from dotenv import load_dotenv
import os
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

#Load .env file
load_dotenv()

api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')

trading_client = TradingClient(api_key, secret_key)

#Get account information
account = trading_client.get_account()

#Check if account is trade-restricted
if account.trading_blocked:
    print('Account is currently restricted from trading.')

#Check how much money we can use to open new positions aka buying power
print ('${} is available as buying power.'.format(account.buying_power))
print ('${} is available as cash.'.format(account.cash))