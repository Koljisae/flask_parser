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
    title = db.Column(db.String(length=20), nullable=False, unique=True)
    api_key = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Numeric(scale=12))
    market_cap = db.Column(db.Numeric(scale=6))
    change_percent = db.Column(db.Numeric(scale=2))
    change_value = db.Column(db.Numeric(scale=6))
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.key_link


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=50), nullable=False)

    def __str__(self):
        return self.title
