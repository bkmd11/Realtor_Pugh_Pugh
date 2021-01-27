from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    listings = db.relationship('Listing', backref='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listing_name = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    ctq = db.relationship('CTQ', backref='list')

    def __repr__(self):
        return '<Listing {}>'.format(self.listing_name)


class CTQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ctq_name = db.Column(db.String(50), unique=True)
    grade = db.Column(db.Integer)
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'))
