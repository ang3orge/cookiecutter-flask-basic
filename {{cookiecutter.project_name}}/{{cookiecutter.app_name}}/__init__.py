from flask import Flask

__version__ = "{{cookiecutter.app_version}}"


def create_app():
    # initialize the flask app
    app = Flask(__name__)

    return app
