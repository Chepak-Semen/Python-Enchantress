from flask import Flask
from pet_hotel.routes import check_in_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(check_in_bp)
    return app
