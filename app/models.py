from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=True)
    last_name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    street_address_one = db.Column(db.String(120), index=True, unique=True)
    street_address_two = db.Column(db.String(120), index=True, unique=True)
    city = db.Column(db.String(64), index=True, unique=True)
    state = db.Column(db.String(64), index=True, unique=True)
    postal_code = db.Column(db.String(5), index=True, unique=True)
    tickers = db.Column(db.String(10), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Profile {self.profile}>'

