from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .config import Config
import os 

app = Flask(__name__)

# Load config first
app.config.from_object(Config)


# Now SQLAlchemy knows the database URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views



