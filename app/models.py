from app import db, login

from flask_login import UserMixin

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.sqlite import JSON

from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    ctq = Column(JSON)

    listings = db.relationship('Listing', backref='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def user_listings(self):
        listings = Listing.query.join(
            User, (User.id == Listing.user_id)
        )


class Listing(db.Model):
    id = Column(Integer, primary_key=True)
    listing_name = Column(String(140))
    user_id = Column(Integer, ForeignKey('user.id'))
    rating = Column(JSON)

    def __repr__(self):

        return '<Listing {}>'.format(self.listing_name)

