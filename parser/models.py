from parser import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=70), nullable=False)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    category = db.Column(db.Integer(), db.ForeignKey('category.id'))
    api_key = db.Column(db.String(length=30), nullable=False, unique=True)

    title = db.Column(db.String(length=20), nullable=False, unique=True)
    max_supply = db.Column(db.Numeric(scale=12))
    date_added = db.Column(db.DateTime)
    price = db.Column(db.Numeric(scale=12))
    market_cap = db.Column(db.Numeric(scale=6))
    percent_change_1h = db.Column(db.Numeric(scale=2))
    percent_change_24h = db.Column(db.Numeric(scale=2))
    percent_change_7d = db.Column(db.Numeric(scale=2))
    percent_change_30d = db.Column(db.Numeric(scale=2))
    percent_change_60d = db.Column(db.Numeric(scale=2))
    percent_change_90d = db.Column(db.Numeric(scale=2))
    volume_24h = db.Column(db.Numeric(scale=6))
    volume_change_24h = db.Column(db.Numeric(scale=6))
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.api_key


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=50), nullable=False)

    def __str__(self):
        return self.title
