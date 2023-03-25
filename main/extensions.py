from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from main.__init__.py import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)
