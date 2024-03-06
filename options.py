from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()
# Your API keys (replace with your actual keys)
api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')

# Alpaca API URL for options snapshots
url = 'https://data.alpaca.markets/v1beta1/options/snapshots/SPY'

# Headers including your API keys for authentication
headers = {
    'APCA-API-KEY-ID': api_key,
    'APCA-API-SECRET-KEY': secret_key,
    'accept': 'application/json'
}

# Function to fetch options data from Alpaca
def fetch_options_data(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Function to find ODTE options
def find_odte_options(data, today_date):
    odte_options = {}
    for identifier, details in data.get('snapshots', {}).items():
        expiration_date = identifier[3:9]  # Extract YYMMDD part
        if expiration_date == today_date:
            odte_options[identifier] = details
    return odte_options

# Get today's date in YYMMDD format
today = datetime.datetime.now().strftime("%y%m%d")  # You may replace this with "240221" for Feb 21, 2024

# Fetch the options data
data = fetch_options_data(url, headers)

# Check if data is not None
if data:
    # Find ODTE options for today
    odte_options_today = find_odte_options(data, today)
    
    # Display or process the ODTE options
    for identifier, details in odte_options_today.items():
        print(f"Identifier: {identifier}, Details: {details}")
else:
    print("Failed to fetch or process data.")