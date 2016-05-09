from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
import config

# Create the flash App and attach a SQLAlchemy db from the DB spec
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# Define the models
class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)

# Create the DB
db.create_all()

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# Create the API endpoints from the DB Models
# These will be available at /api/<tablename>
manager.create_api(Beer, methods=['GET', 'POST', 'PUT', 'DELETE'])

# start the flask app
app.run(debug=True)
