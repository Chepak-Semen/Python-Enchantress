from flask import Flask
from flask_restful import Api

from restfull_cart import Cart

amazon_killer = Flask(__name__)

api = Api(amazon_killer)
api.add_resource(Cart, "/cart", '/cart/<int:cart_id>')

if __name__ == '__main__':
    amazon_killer.run()
