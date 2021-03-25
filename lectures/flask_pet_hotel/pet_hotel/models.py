from . import db


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    phone_number = db.Column(db.String(20), unique=True)


class Pet(db.Model):
    owner = db.relationship('Owner', backref='pet')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    room_id = db.Column(db.Integer)
    date = db.Column(db.Date)


class Activities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30))
    time = db.Column(db.String(30))
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
