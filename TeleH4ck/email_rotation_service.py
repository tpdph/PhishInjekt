import logging
import requests

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

# Set up the email rotation service
email_service = 'https://api.mailgun.net'

# Define the get_email function
def get_email():
    # Use the Mailgun API to get an email address
    api_key = 'YOUR_API_KEY'
    try:
        response = requests.post(f'{email_service}/v3/emails', headers={'Authorization': f'Bearer {api_key}'}, json={'address': 'example@example.com'})
        response.raise_for_status()
        email = response.json()['address']
        logging.info(f"Successfully retrieved email: {email}")
        return email
    except requests.exceptions.RequestException as e:
        logging.error(f"Error retrieving email: {e}")
        return None
