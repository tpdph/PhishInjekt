import sqlite3
import yaml
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

# Load configuration
try:
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
except Exception as e:
    logging.error(f"Error loading configuration: {e}")
    exit()

# Function to store a report in the database
def store_report_in_db(report_type, report_data):
    try:
        conn = sqlite3.connect(config['database']['path'])
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reports (report_type, report_data) VALUES (?, ?)", (report_type, str(report_data)))
        conn.commit()
        conn.close()
        logging.info(f"Successfully stored report of type '{report_type}' in database.")
        return True
    except Exception as e:
        logging.error(f"Error storing report in database: {e}")
        return False

# Function to send a report (currently stores in database)
def send_report(report):
    if store_report_in_db(report['type'], report['data']):
        logging.info(f"Report of type '{report['type']}' processed successfully.")
        return True
    else:
        logging.error(f"Failed to process report of type '{report['type']}'.")
        return False

# Main function for testing
if __name__ == '__main__':
    # Example Usage
    report_data = {"username": "testuser", "activity": "failed login"}
    if store_report_in_db("login_failure", report_data):
        logging.info("Test report stored successfully.")
    else:
        logging.error("Failed to store test report.")
