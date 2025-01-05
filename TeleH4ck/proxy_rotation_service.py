import logging
import requests

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

# Set up the proxy rotation service
proxy_service = 'https://api.proxyrack.com'

# Define the get_proxy function
def get_proxy():
    # Use the ProxyRack API to get a proxy
    api_key = 'YOUR_API_KEY'
    try:
        response = requests.get(f'{proxy_service}/get_proxy', headers={'Authorization': f'Bearer {api_key}'})
        response.raise_for_status()
        proxy = response.json()['proxy']
        logging.info(f"Successfully retrieved proxy: {proxy}")
        return proxy
    except requests.exceptions.RequestException as e:
        logging.error(f"Error retrieving proxy: {e}")
        return None
