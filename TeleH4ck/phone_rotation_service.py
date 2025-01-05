import logging
import requests

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

# Set up the phone rotation service
phone_service = 'https://api.twilio.com'

# Define the get_phone function
def get_phone():
    # Use the Twilio API to get a phone number
    account_sid = 'YOUR_ACCOUNT_SID'
    auth_token = 'YOUR_AUTH_TOKEN'
    try:
        response = requests.post(f'{phone_service}/2010-04-01/Accounts/{{account_sid}}/IncomingPhoneNumbers.json', headers={'Authorization': f'Bearer {auth_token}'}, json={'PhoneNumber': '+1234567890'})
        response.raise_for_status()
        phone = response.json()['phone_number']
        logging.info(f"Successfully retrieved phone number: {phone}")
        return phone
    except requests.exceptions.RequestException as e:
        logging.error(f"Error retrieving phone number: {e}")
        return None
