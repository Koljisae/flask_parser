import os
from dotenv import load_dotenv

load_dotenv()


# COINMARKETCAP API
TEST_API_CRYPTO_URL = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
# API_CRYPTO_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
API_CRYPTO_URL = TEST_API_CRYPTO_URL
HEADERS = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('API_KEY'),
}


# CONSTANTS FOR DATABASES
CATEGORIES = (
    {'id': 1, 'title': 'currency'},
    {'id': 2, 'title': 'crypto'},
    {'id': 3, 'title': 'stock'},
)
CRYPTO = (
    {
        'category': 2,
        'title': 'Bitcoin',
        'api_key': 'BTC',
    },
    {
        'category': 2,
        'title': 'Ethereum',
        'api_key': 'ETH',
    },
    {
        'category': 2,
        'title': 'Tether USDt',
        'api_key': 'USDT',
    },
    {
        'category': 2,
        'title': 'BNB',
        'api_key': 'BNB',
    },
    {
        'category': 2,
        'title': 'USD Coin',
        'api_key': 'USDC',
    },
    {
        'category': 2,
        'title': 'Dogecoin',
        'api_key': 'DOGE',
    },
    {
        'category': 2,
        'title': 'Cardano',
        'api_key': 'ADA',
    },
    {
        'category': 2,
        'title': 'Solana',
        'api_key': 'SOL',
    },
    {
        'category': 2,
        'title': 'TRON',
        'api_key': 'TRX',
    },
    {
        'category': 2,
        'title': 'Litecoin',
        'api_key': 'LTC',
    },
    {
        'category': 2,
        'title': 'Shiba Inu',
        'api_key': 'SHIB',
    },
    {
        'category': 2,
        'title': 'Monero',
        'api_key': 'XMR',
    },
)
