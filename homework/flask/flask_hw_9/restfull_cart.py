"""Tre to do CART with using RESTFUL"""
from datetime import datetime

from flask import request
from flask_restful import Resource

CART_DATABASE = {}
cart_counter = 1


class NoSuchUser(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


def is_user_in_db(user_id, db):
    """check availability user in DB"""
    if user_id in db:
        return True
    else:
        raise KeyError


class Cart(Resource):
    @staticmethod
    def post():
        """create new cart in CARTS_DB/ return dict & status code"""
        global cart_counter
        cart = request.json
        user_id = cart["user_id"]
        response = {
            "user_id": cart_counter,
            "registration_timestamp": datetime.now().isoformat(),
        }
        try:
            is_user_in_db(user_id, CART_DATABASE)
        except NoSuchUser:
            return {"error": f"no such user "}, 404
        else:
            CART_DATABASE[cart_counter] = response
            cart_counter += 1
            return response, 201

    @staticmethod
    def get(cart_id):
        """read cart info from DB return dict"""
        try:
            user = CART_DATABASE[cart_id]
        except KeyError:
            return {"error": f"no such user "}, 404
        else:
            return user

    @staticmethod
    def put(cart_id):
        """change info in CART_DB/ return dict(response) & status code"""
        put_data = request.json
        response = {"status": "success"}
        try:
            CART_DATABASE[cart_id]["products"] = put_data["products"]
        except KeyError:
            return {"error": f"no such user "}, 404
        else:
            return response, 200

    @staticmethod
    def delete(cart_id):
        """delete cart from CARTS_DB using key=cart_id/ return dict(response) & status code"""
        response = {"status": "success"}
        try:
            CART_DATABASE.pop(cart_id)
        except KeyError:
            return {"error": f"no such user "}, 404
        else:
            return response, 200
