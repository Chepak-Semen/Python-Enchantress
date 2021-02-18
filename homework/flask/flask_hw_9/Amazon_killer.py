from flask import Flask
from flask_restful import Api

from blueptints_user import users_bd
from restfull_cart import Cart

amazon_killer = Flask(__name__)

amazon_killer.register_blueprint(users_bd, url_prefix="/users")

api = Api(amazon_killer)
api.add_resource(Cart, "/cart", '/cart/<int:cart_id>')
