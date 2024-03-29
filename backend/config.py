from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from env import (DATABASE_URI, SECRET_KEY)
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # setting up Cross Origin Resource Sharing
    CORS(app)

    # setting up db
    db.init_app(app)

    # setting up migration
    migrate.init_app(app, db)

    return app
