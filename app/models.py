from app import db

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.sqlite import JSON


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    ctq = Column(JSON)

    listings = db.relationship('Listing', backref='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Listing(db.Model):
    id = Column(Integer, primary_key=True)
    listing_name = Column(String(140))
    user_id = Column(Integer, ForeignKey('user.id'))
    rating = Column(JSON)

    def __repr__(self):

        return '<Listing {}>'.format(self.listing_name)

