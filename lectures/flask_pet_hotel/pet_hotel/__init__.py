from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .middleware import OurMiddleware


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.wsgi_app = OurMiddleware(app.wsgi_app)
    app.config['SECRET_KEY'] = 'key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'

    db.init_app(app=app)

    from .routes import ShowActivities, SetDeletePet
    api.add_resource(ShowActivities, '/show_activ')
    api.add_resource(SetDeletePet, '/set_pet')

    return app
