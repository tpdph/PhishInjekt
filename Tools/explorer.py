import os
import tkinter as tk
from tkinter import ttk, Label, Entry, Button, Toplevel, Text, Scrollbar, messagebox

def create_ssh_connection_window(explorer_tab):
    connection_window = Toplevel(explorer_tab)
    connection_window.title("SSH Connection")

    Label(connection_window, text="IP Address:").grid(row=0, column=0, sticky="e")
    ip_entry = Entry(connection_window)
    ip_entry.grid(row=0, column=1)

    Label(connection_window, text="Username:").grid(row=1, column=0, sticky="e")
    username_entry = Entry(connection_window)
    username_entry.grid(row=1, column=1)

    Label(connection_window, text="Password:").grid(row=2, column=0, sticky="e")
    password_entry = Entry(connection_window, show="*")
    password_entry.grid(row=2, column=1)
    
    connect_button = Button(connection_window, text="Connect", command=lambda: connect_ssh(ip_entry, username_entry, password_entry, connection_window, explorer_tab))
    connect_button.grid(row=3, column=1, pady=10)

def connect_ssh(ip_entry, username_entry, password_entry, connection_window, explorer_tab):
    ip_address = ip_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    # Call the remote_connection function from app.py
    # Assuming app.py is accessible or imported
    messagebox.showinfo("Success", "SSH connection established.")
    file_browser_button = next((child for child in explorer_tab.winfo_children() if child.winfo_name() == "file_browser_button"), None)
    process_list_button = next((child for child in explorer_tab.winfo_children() if child.winfo_name() == "process_list_button"), None)
    if file_browser_button:
        file_browser_button.config(state="normal")
    if process_list_button:
        process_list_button.config(state="normal")
    else:
        messagebox.showerror("Error", "Failed to establish SSH connection.")
    connection_window.destroy()

def create_file_browser_window(explorer_tab, ssh_client):
    if not ssh_client:
        messagebox.showerror("Error", "No SSH connection established.")
        return
    
    browser_window = Toplevel(explorer_tab)
    browser_window.title("File Browser")
    
    initial_path = os.getcwd()
    # Call the file_browser function from app.py
    files = [] # Replace with actual call
    
    text_area = Text(browser_window, wrap="word", height=20, width=80)
    text_area.insert("1.0", "\n".join(files))
    text_area.config(state="disabled")
    text_area.pack(pady=10, padx=10)

def create_process_list_window(explorer_tab, ssh_client):
    if not ssh_client:
        messagebox.showerror("Error", "No SSH connection established.")
        return
    
    process_window = Toplevel(explorer_tab)
    process_window.title("Process List")
    
    # Call the process_list function from app.py
    processes = "" # Replace with actual call
    
    text_area = Text(process_window, wrap="word", height=20, width=80)
    text_area.insert("1.0", processes)
    text_area.config(state="disabled")
    text_area.pack(pady=10, padx=10)

def start_keylogger():
    # Call the keylogger function from app.py
    pass

def start_screen_mirroring():
    # Call the screen_mirroring function from app.py
    pass

def setup_explorer_gui(explorer_tab):
    ssh_button = ttk.Button(explorer_tab, text="SSH Connection", command=lambda: create_ssh_connection_window(explorer_tab))
    ssh_button.pack(pady=5, padx=5)
    ssh_button.bind("<Enter>", lambda e: ssh_button.config(text="Establish a remote SSH connection"))
    ssh_button.bind("<Leave>", lambda e: ssh_button.config(text="SSH Connection"))

    file_browser_button = ttk.Button(explorer_tab, text="File Browser", command=lambda: create_file_browser_window(explorer_tab, None), state="disabled", name="file_browser_button")
    file_browser_button.pack(pady=5, padx=5)
    file_browser_button.bind("<Enter>", lambda e: file_browser_button.config(text="Browse files on the remote machine"))
    file_browser_button.bind("<Leave>", lambda e: file_browser_button.config(text="File Browser"))

    process_list_button = ttk.Button(explorer_tab, text="Process List", command=lambda: create_process_list_window(explorer_tab, None), state="disabled", name="process_list_button")
    process_list_button.pack(pady=5, padx=5)
    process_list_button.bind("<Enter>", lambda e: process_list_button.config(text="View running processes on the remote machine"))
    process_list_button.bind("<Leave>", lambda e: process_list_button.config(text="Process List"))

    keylogger_button = ttk.Button(explorer_tab, text="Keylogger", command=start_keylogger)
    keylogger_button.pack(pady=5, padx=5)
    keylogger_button.bind("<Enter>", lambda e: keylogger_button.config(text="Start keylogger on the local machine"))
    keylogger_button.bind("<Leave>", lambda e: keylogger_button.config(text="Keylogger"))

    screen_mirroring_button = ttk.Button(explorer_tab, text="Screen Mirroring", command=start_screen_mirroring)
    screen_mirroring_button.pack(pady=5, padx=5)
    screen_mirroring_button.bind("<Enter>", lambda e: screen_mirroring_button.config(text="Take a screenshot of the local machine"))
    screen_mirroring_button.bind("<Leave>", lambda e: screen_mirroring_button.config(text="Screen Mirroring"))
import os
import paramiko
import pyautogui
import keyboard
import subprocess
import tkinter as tk
from tkinter import ttk, Label, Entry, Button, Toplevel, Text, Scrollbar, messagebox

def remote_connection(ip_address, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ip_address, username=username, password=password)
    return ssh_client

def file_browser(ssh_client, initial_path):
    current_path = initial_path
    files = []
    if ssh_client:
        stdin, stdout, stderr = ssh_client.exec_command(f'ls {current_path}')
        files = stdout.read().decode().splitlines()
    else:
        files = os.listdir(current_path)
    return files

def process_list(ssh_client):
    if ssh_client:
        stdin, stdout, stderr = ssh_client.exec_command('ps aux')
        return stdout.read().decode()
    else:
        process = subprocess.Popen('ps aux', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            return f"Error running command: {stderr.decode()}"
        else:
            return stdout.decode()

def keylogger():
    print("Keylogger started. Logging to keylog.txt")
    with open("keylog.txt", "a") as f:
        def on_key_press(event):
            f.write(event.name + "\n")
        keyboard.hook(on_key_press)
        keyboard.wait()
        keyboard.unhook(on_key_press)

def screen_mirroring():
    print("Screen mirroring started.")
    screenshot = pyautogui.screenshot()
    timestamp = str(int(time.time()))
    screenshot_path = os.path.join(os.getcwd(), f"screenshot_{timestamp}.png")
    screenshot.save(screenshot_path)
    return screenshot_path

def create_ssh_connection_window(explorer_tab):
    connection_window = Toplevel(explorer_tab)
    connection_window.title("SSH Connection")

    Label(connection_window, text="IP Address:").grid(row=0, column=0, sticky="e")
    ip_entry = Entry(connection_window)
    ip_entry.grid(row=0, column=1)

    Label(connection_window, text="Username:").grid(row=1, column=0, sticky="e")
    username_entry = Entry(connection_window)
    username_entry.grid(row=1, column=1)

    Label(connection_window, text="Password:").grid(row=2, column=0, sticky="e")
    password_entry = Entry(connection_window, show="*")
    password_entry.grid(row=2, column=1)
    
    connect_button = Button(connection_window, text="Connect", command=lambda: connect_ssh(ip_entry, username_entry, password_entry, connection_window, explorer_tab))
    connect_button.grid(row=3, column=1, pady=10)

def connect_ssh(ip_entry, username_entry, password_entry, connection_window, explorer_tab):
    ip_address = ip_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    ssh_client = remote_connection(ip_address, username, password)
    if ssh_client:
        messagebox.showinfo("Success", "SSH connection established.")
        file_browser_button = next((child for child in explorer_tab.winfo_children() if child.winfo_name() == "file_browser_button"), None)
        process_list_button = next((child for child in explorer_tab.winfo_children() if child.winfo_name() == "process_list_button"), None)
        if file_browser_button:
            file_browser_button.config(state="normal")
        if process_list_button:
            process_list_button.config(state="normal")
    else:
        messagebox.showerror("Error", "Failed to establish SSH connection.")
    connection_window.destroy()

def create_file_browser_window(explorer_tab, ssh_client):
    if not ssh_client:
        messagebox.showerror("Error", "No SSH connection established.")
        return
    
    browser_window = Toplevel(explorer_tab)
    browser_window.title("File Browser")
    
    initial_path = os.getcwd()
    files = file_browser(ssh_client, initial_path)
    
    text_area = Text(browser_window, wrap="word", height=20, width=80)
    text_area.insert("1.0", "\n".join(files))
    text_area.config(state="disabled")
    text_area.pack(pady=10, padx=10)

def create_process_list_window(explorer_tab, ssh_client):
    if not ssh_client:
        messagebox.showerror("Error", "No SSH connection established.")
        return
    
    process_window = Toplevel(explorer_tab)
    process_window.title("Process List")
    
    processes = process_list(ssh_client)
    
    text_area = Text(process_window, wrap="word", height=20, width=80)
    text_area.insert("1.0", processes)
    text_area.config(state="disabled")
    text_area.pack(pady=10, padx=10)

def start_keylogger():
    keylogger()

def start_screen_mirroring():
    screenshot_path = screen_mirroring()
    messagebox.showinfo("Screen Mirroring", f"Screenshot saved to {screenshot_path}")

def setup_explorer_gui(explorer_tab):
    ssh_button = ttk.Button(explorer_tab, text="SSH Connection", command=lambda: create_ssh_connection_window(explorer_tab))
    ssh_button.pack(pady=5, padx=5)
    ssh_button.bind("<Enter>", lambda e: ssh_button.config(text="Establish a remote SSH connection"))
    ssh_button.bind("<Leave>", lambda e: ssh_button.config(text="SSH Connection"))

    file_browser_button = ttk.Button(explorer_tab, text="File Browser", command=lambda: create_file_browser_window(explorer_tab, None), state="disabled", name="file_browser_button")
    file_browser_button.pack(pady=5, padx=5)
    file_browser_button.bind("<Enter>", lambda e: file_browser_button.config(text="Browse files on the remote machine"))
    file_browser_button.bind("<Leave>", lambda e: file_browser_button.config(text="File Browser"))

    process_list_button = ttk.Button(explorer_tab, text="Process List", command=lambda: create_process_list_window(explorer_tab, None), state="disabled", name="process_list_button")
    process_list_button.pack(pady=5, padx=5)
    process_list_button.bind("<Enter>", lambda e: process_list_button.config(text="View running processes on the remote machine"))
    process_list_button.bind("<Leave>", lambda e: process_list_button.config(text="Process List"))

    keylogger_button = ttk.Button(explorer_tab, text="Keylogger", command=start_keylogger)
    keylogger_button.pack(pady=5, padx=5)
    keylogger_button.bind("<Enter>", lambda e: keylogger_button.config(text="Start keylogger on the local machine"))
    keylogger_button.bind("<Leave>", lambda e: keylogger_button.config(text="Keylogger"))

    screen_mirroring_button = ttk.Button(explorer_tab, text="Screen Mirroring", command=start_screen_mirroring)
    screen_mirroring_button.pack(pady=5, padx=5)
    screen_mirroring_button.bind("<Enter>", lambda e: screen_mirroring_button.config(text="Take a screenshot of the local machine"))
    screen_mirroring_button.bind("<Leave>", lambda e: screen_mirroring_button.config(text="Screen Mirroring"))
