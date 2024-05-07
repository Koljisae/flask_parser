import os
from dotenv import load_dotenv

load_dotenv()


# COINMARKETCAP API
API_CRYPTO_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
# TEST_API_CRYPTO_URL = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
# API_CRYPTO_URL = TEST_API_CRYPTO_URL
HEADERS = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('API_KEY'),
}


# CONSTANTS FOR DATABASE
CATEGORIES = (
    {'id': 1, 'title': 'currency'},
    {'id': 2, 'title': 'crypto'},
    {'id': 3, 'title': 'stock'},
)
CRYPTO = [
    'BTC',
    'ETH',
    'USDT',
    'BNB',
    'USDC',
    'DOGE',
    'ADA',
    'SOL',
    'TRX',
    'LTC',
    'XMR',
]
