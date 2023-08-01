import requests
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, Blueprint
from bs4 import BeautifulSoup as bs
from flask_login import current_user
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from parser.conf import API_CRYPTO_URL, HEADERS
from parser.models import Item, Category, User
from parser import db

views = Blueprint('views', __name__)


def get_crypto_data(api_key: str):
    parameters = {
        'symbol': api_key,
        'convert': 'USD',
    }
    session = Session()
    session.headers.update(HEADERS)
    try:
        response = session.get(API_CRYPTO_URL, params=parameters)
        if response.status_code == 200:
            data = json.loads(response.text)['data'][api_key]['quote']['USD']
            price = data.get('price')
            market_cap = data.get('market_cap')
            change_percent = data.get('percent_change_24h')
            change_value = data.get('volume_change_24h')
            last_updated = data.get('last_updated')
            last_updated = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
            return {
                'price': price,
                'market_cap': market_cap,
                'change_percent': change_percent,
                'change_value': change_value,
                'last_updated': last_updated,
            }
        else:
            return 'Bad request.'
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e


@views.route('/home')
@views.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('home.html', current_user=current_user)
    else:
        return redirect(url_for('auth.user_login'))
