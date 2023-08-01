from flask import Blueprint
from flask.cli import with_appcontext

from parser import db
from parser.conf import CATEGORIES, CRYPTO
from parser.models import Item, Category
from parser.views import get_crypto_data

commands = Blueprint('commands', __name__)


@commands.cli.command(name='create_categories')
@with_appcontext
def create_categories():
    for category in CATEGORIES:
        title = category.get('title')
        if not Category.query.filter_by(
            id=category.get('id'),
            title=title,
        ).first():
            category_model = Category(**category)
            db.session.add(category_model)
            db.session.commit()
            print(f'Category "{title}" added.')
        else:
            print(f'Category "{title}" already exists.')


@commands.cli.command(name='create_crypto_items')
@with_appcontext
def create_crypto_items():
    for item in CRYPTO:
        title = item.get('title')
        api_key = item.get('api_key')
        if not Item.query.filter_by(
            category=item.get('category'),
            title=title,
            api_key=api_key
        ).first():
            values = get_crypto_data(api_key)
            item_model = Item(**item, **values)
            db.session.add(item_model)
            db.session.commit()
            print(f'Crypto "{title}" added.')
        else:
            print(f'Crypto "{title}" already exists.')
