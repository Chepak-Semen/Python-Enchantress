from datetime import datetime, date

from flask import request
from flask_restful import Resource

from models import Owner, Pet, Activities
from . import db


class SetDeletePet(Resource):

    @staticmethod
    def post():
        response = request.get_json()
        db.session.add(Owner(name=response["name"],
                             phone_number=response["phone_number"]
                             ))
        added_user = Owner.query.filter_by(name=response["name"],
                                           phone_number=response["phone_number"]
                                           ).first()
        db.session.commit()
        db.session.add(Pet(name=response["pet"]['name'],
                           owner_id=added_user.id,
                           room_id=response['pet']["room_id"],
                           date=datetime.now(),
                           ))
        db.session.commit()
        added_pet = Pet.query.filter_by(owner_id=added_user.id).first()
        db.session.add(Activities(type=response['pet']["activity"]["activity_type"],
                                  time=response['pet']["activity"]["time"],
                                  pet_id=added_pet.id))
        db.session.commit()
        return {"status": "success"}, 201

    @staticmethod
    def delete():
        response = request.get_json()
        pet = Pet.query.filter_by(name=response["pet_name"], room_id=response["room_id"]).first()
        owner_pet = Pet.query.filter_by(owner_id=pet.owner.id).all()
        pet_activities = Activities.query.filter_by(pet_id=pet.id).all()

        db.session.delete(pet)
        db.session.delete(pet_activities)
        db.session.commit()

        if not owner_pet:
            db.session.delete(Owner.query.filter_by(id=pet.owner.id).delete())
            db.session.commit()

        return (date.today() - pet.date).days, 200


class ShowActivities(Resource):

    @staticmethod
    def post():
        actv = []
        response = request.get_json()
        pet = Pet.query.filter_by(name=response["pet_name"]).first()
        activities = Activities.query.filter_by(id=pet.id).all()
        for i in activities:
            actv.append({pet.name: {'type': i.type, 'hour': i.time}})
        return actv

