from flask import Flask
from flask_smorest import Api
from db import db

from resources.item import blp as ItemBluePrint
from resources.store import blp as StoreBluePrint


def create_app():

    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"]= True
    app.config["API_TITLE"] = 'Stores REST API'
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_NOTIFICATION"]=False

    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBluePrint)
    api.register_blueprint(StoreBluePrint)

    return app


