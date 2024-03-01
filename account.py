from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient('api-key', 'secret-key')

#Get account information
account = trading_client.get_account()

#Check if account is trade-restricted
if account.trading_blocked:
    print('Account is currently restricted from trading.')

#Check how much money we can use to open new positions aka buying power
print ('${} is available as buying power.'.format(account.buying_power))