from flask import Flask
from app import views


def create_app(config_object="app.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(views.views.blueprint, url_prefix='/')
    return app
