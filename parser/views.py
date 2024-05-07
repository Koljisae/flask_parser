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
            data = json.loads(response.text)['data'][api_key]
            name = data.get('name')
            max_supply = data.get('max_supply')
            date_added = data.get('date_added')
            date_added = datetime.fromisoformat(date_added.replace('Z', '+00:00'))

            data = data['quote']['USD']
            price = data.get('price')
            market_cap = data.get('market_cap')
            percent_change_1h = data.get('percent_change_1h')
            percent_change_24h = data.get('percent_change_24h')
            percent_change_7d = data.get('percent_change_7d')
            percent_change_30d = data.get('percent_change_30d')
            percent_change_60d = data.get('percent_change_60d')
            percent_change_90d = data.get('percent_change_90d')
            volume_24h = data.get('volume_24h')
            volume_change_24h = data.get('volume_change_24h')
            last_updated = data.get('last_updated')
            last_updated = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
            return {
                'title': name,
                'max_supply': max_supply,
                'date_added': date_added,
                'price': price,
                'market_cap': market_cap,
                'percent_change_1h': percent_change_1h,
                'percent_change_24h': percent_change_24h,
                'percent_change_7d': percent_change_7d,
                'percent_change_30d': percent_change_30d,
                'percent_change_60d': percent_change_60d,
                'percent_change_90d': percent_change_90d,
                'volume_24h': volume_24h,
                'volume_change_24h': volume_change_24h,
                'last_updated': last_updated,
            }
        else:
            return 'Bad request.'
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e


@views.route('/home/<int:page>', methods=['GET'])
@views.route('/<int:page>', methods=['GET'])
@views.route('/home', methods=['GET'])
@views.route('/', methods=['GET'])
def home(page: int = 1):
    per_page = 10
    currencies = Item.query.filter_by(category=2).paginate(page=page, per_page=per_page, error_out=False)
    return render_template('home.html', currencies=currencies, title='Home')


@views.route('/update', methods=['GET'])
def update_crypto():
    currencies = Item.query.filter_by(category=2)
    for currency in currencies:
        data = get_crypto_data(currency.api_key)
        currency.title = data.get('title')
        currency.max_supply = data.get('max_supply')
        currency.date_added = data.get('date_added')
        currency.price = data.get('price')
        currency.market_cap = data.get('market_cap')
        currency.percent_change_1h = data.get('percent_change_1h')
        currency.percent_change_24h = data.get('percent_change_24h')
        currency.percent_change_7d = data.get('percent_change_7d')
        currency.percent_change_30d = data.get('percent_change_30d')
        currency.percent_change_60d = data.get('percent_change_60d')
        currency.percent_change_90d = data.get('percent_change_90d')
        currency.volume_24h = data.get('volume_24h')
        currency.volume_change_24h = data.get('volume_change_24h')
        currency.last_updated = data.get('last_updated')
        db.session.commit()
    return redirect(url_for('views.home', title='Update crypto'))


@views.route('/detail/<string:api_key>', methods=['GET'])
def detail_crypto(api_key=None):
    currency = Item.query.filter_by(api_key=api_key, category=2).first()
    return render_template('detail.html', currency=currency, title=f'{currency.title} details')
