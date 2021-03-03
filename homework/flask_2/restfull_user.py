from datetime import datetime

from flask import Blueprint, request
from flask_restful import Resource

users_bd = Blueprint('users', __name__)
USERS_DATABASE = {}
user_counter = 1


def is_user_in_db(user_id, db):
    """check availability user in DB"""
    if user_id in db:
        return True
    else:
        raise KeyError


class User(Resource):

    @staticmethod
    def post():
        """create new user in USERS_DB/ return dict & status code"""
        global user_counter
        user = request.json
        user['user_id'] = user_counter
        response = {
            "registration_timestamp": datetime.now().isoformat(),
            "user_id": user_counter
        }
        user["registration_timestamp"] = response['registration_timestamp']
        USERS_DATABASE[user_counter] = user

        user_counter += 1

        return response, 201

    @staticmethod
    def get(user_id):
        """read user info from DB return dict"""
        try:
            user = USERS_DATABASE.get("user_id")
        except KeyError:
            return {"error": f"no such user with id {user_id}"}, 404
        else:
            return user

    @staticmethod
    def put(user_id):
        """change info in USERS_DB/ return dict(response) & status code"""
        put_data = request.json
        response = {"status": "success"}
        try:
            is_user_in_db(user_id, USERS_DATABASE)
            user = USERS_DATABASE[user_id]
            user["name"] = put_data["name"]
            user["email"] = put_data["email"]
        except KeyError:
            return {"error": f"no such user with id {user_id}"}, 404
        else:
            return response, 200

    @staticmethod
    def delete(user_id):
        """delete user from USERS_DB using key=user_id/ return dict(response) & status code"""
        response = {"status": "success"}
        try:
            USERS_DATABASE.pop(user_id)
        except KeyError:
            return {"error": f"no such user with id {user_id}"}, 404
        else:
            return response, 200
