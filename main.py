import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv('CLOUDFLARE_API_TOKEN')

# Define headers for the API requests, including the Authorization token and the content type.
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}


# Function to fetch user details from Cloudflare's API
def fetch_user_details():
    # Define the URL for the user details endpoint
    url = 'https://api.cloudflare.com/client/v4/user'
    # Send a GET request to the specified URL, with the defined headers
    response = requests.get(url, headers=headers)
    # Check if the response status code is 200 (OK)
    if response.ok:
        # Parse the JSON response and print it
        data = response.json()
        print(data)
    else:
        # If the response status code is not 200, print the error status code and response text
        print(f'Error: {response.status_code}')
        print(response.text)


# Function to list zones in Cloudflare's account
def list_zones():
    # Define the URL for the zones listing endpoint
    url = 'https://api.cloudflare.com/client/v4/zones'
    # Send a GET request to the specified URL, with the defined headers
    response = requests.get(url, headers=headers)
    # Check if the response status code is 200 (OK)
    if response.ok:
        # Parse the JSON response and print it
        data = response.json()
        print(data)
    else:
        # If the response status code is not 200, print the error status code and response text
        print(f'Error: {response.status_code}')
        print(response.text)


# Function to create a DNS record in a specified zone
def create_dns_record(zone_id, dns_record_data):
    # Define the URL for the DNS record creation endpoint, including the specified zone ID
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    # Send a POST request to the specified URL, with the defined headers and JSON payload
    response = requests.post(url, headers=headers, json=dns_record_data)
    # Check if the response status code is 200 (OK)
    if response.ok:
        # Parse the JSON response and print it
        data = response.json()
        print(data)
    else:
        # If the response status code is not 200, print the error status code and response text
        print(f'Error: {response.status_code}')
        print(response.text)


# Main execution starts here when the script is run
if __name__ == "__main__":
    # Example usage of the defined functions
    fetch_user_details()  # Fetch and print user details
    list_zones()  # List and print zones
    # Create and print a new DNS record in a specified zone
    create_dns_record('your-zone-id-here', {
        'type': 'A',
        'name': 'example.com',
        'content': '192.0.2.1',
        'ttl': 120,
    })
