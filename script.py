import requests
import os
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_public_ip():
    try:
        # Use a service to get your public IP address
        response = requests.get('https://api64.ipify.org?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except Exception as e:
        logging.error(f"Error getting public IP: {e}")
        return None

def read_last_ip():
    try:
        # Read the last recorded public IP from a file
        with open('last_ip.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def write_last_ip(public_ip):
    try:
        # Write the current public IP to a file
        with open('last_ip.txt', 'w') as file:
            file.write(public_ip)
    except Exception as e:
        logging.error(f"Error writing last IP to file: {e}")

def update_duckdns(public_ip, duckdns_token, domain):
    try:
        # Update DuckDNS only if the public IP has changed
        last_ip = read_last_ip()

        if public_ip != last_ip:
            duckdns_url = f'https://www.duckdns.org/update?domains={domain}&token={duckdns_token}&ip={public_ip}'
            response = requests.get(duckdns_url)

            if response.text == 'OK':
                logging.info(f"IP address updated successfully to {public_ip}")
                write_last_ip(public_ip)  # Update last recorded IP
            else:
                logging.error(f"Failed to update IP address. DuckDNS response: {response.text}")
        else:
            logging.info(f"IP address is UP TO DATE | local: {public_ip}  DuckDNS: {last_ip}")
    except Exception as e:
        logging.error(f"Error updating DuckDNS: {e}")

if __name__ == "__main__":
    duckdns_token = os.getenv('DUCKDNS_TOKEN')
    domain = os.getenv('DUCKDNS_DOMAIN')

    if not duckdns_token or not domain:
        logging.error("Error: Please set DUCKDNS_TOKEN and DUCKDNS_DOMAIN environment variables.")
        exit(1)

    # Run the script in a loop every 10 minutes
    while True:
        # Get public IP address
        public_ip = get_public_ip()

        if public_ip:
            # Update DuckDNS only if the public IP has changed
            update_duckdns(public_ip, duckdns_token, domain)

        # Sleep for 10 minutes before the next iteration
        time.sleep(300)  # 600 seconds = 10 minutes
