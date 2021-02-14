from datetime import datetime

from flask import Flask, request

amazon_killer = Flask(__name__)

CART_DATABASE = {}
USERS_DATABASE = {}
user_counter = 1
cart_counter = 1


class NoSuchUser(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


def is_user_in_db(user_id):
    """check availability user in DB"""
    return True if user_id in USERS_DATABASE else False


@amazon_killer.route('/users', methods=["POST"])
def create_user():
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


@amazon_killer.errorhandler(NoSuchUser)
def no_such_user_handler(e):
    return {"error": f"no such user with id {e.user_id}"}, 404


@amazon_killer.route('/users/<int:user_id>')
def get_user(user_id):
    """read user info from DB return dict"""
    try:
        user = USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        return user


@amazon_killer.route('/users/<int:user_id>', methods=["PUT"])
def put_user(user_id):
    """change info in USERS_DB/ return dict(response) & status code"""
    put_data = request.json
    response = {"status": "success"}
    try:
        is_user_in_db(user_id)
        user = USERS_DATABASE[user_id]
        user["name"] = put_data["name"]
        user["email"] = put_data["email"]
    except False or KeyError:
        raise NoSuchUser
    else:
        return response, 200


@amazon_killer.route('/users/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
    """delete user from USERS_DB using key=user_id/ return dict(response) & status code"""
    response = {"status": "success"}
    try:
        USERS_DATABASE.pop(user_id)
    except KeyError:
        raise NoSuchUser
    else:
        return response, 200





@amazon_killer.route('/cart', methods=["POST"])
def create_cart():
    """create new cart in CARTS_DB/ return dict & status code"""
    global cart_counter
    cart = request.json
    user_id = cart["user_id"]
    response = {
        "user_id": cart_counter,
        "registration_timestamp": datetime.now().isoformat(),
    }
    try:
        is_user_in_db(user_id)
    except False:
        raise NoSuchUser(user_id)
    else:
        CART_DATABASE[cart_counter] = response
        cart_counter += 1
        return response, 201


@amazon_killer.route('/cart/<int:cart_id>')
def get_cart(cart_id):
    """read cart info from DB return dict"""
    try:
        user = CART_DATABASE[cart_id]
    except KeyError:
        raise NoSuchUser(cart_id)
    else:
        return user


@amazon_killer.route('/cart/<int:cart_id>', methods=["PUT"])
def put_cart(cart_id):
    """change info in CART_DB/ return dict(response) & status code"""
    put_data = request.json
    response = {"status": "success"}
    try:
        CART_DATABASE[cart_id]["products"] = put_data["products"]
    except KeyError:
        raise NoSuchUser
    else:
        return response, 200


@amazon_killer.route('/cart/<int:cart_id>', methods=["DELETE"])
def delete_cart(cart_id):
    """delete cart from CARTS_DB using key=cart_id/ return dict(response) & status code"""
    response = {"status": "success"}
    try:
        CART_DATABASE.pop(cart_id)
    except KeyError:
        raise NoSuchUser
    else:
        return response, 200


if __name__ == '__main__':
    amazon_killer.run(debug=True)
