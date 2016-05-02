from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

# Create the flash App and attach a SQLAlchemy db from the DB spec
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Define the models
class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))
    reviews = db.relationship('Review', backref=db.backref('beer'), lazy='dynamic')

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    beers = db.relationship('Beer', backref=db.backref('type'), lazy='dynamic')

class Reviewer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    reviews = db.relationship('Review', backref=db.backref('author'), lazy='dynamic')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    stars = db.Column(db.Float)
    comment = db.Column(db.Unicode)
    beer_id = db.Column(db.Integer, db.ForeignKey('beer.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('reviewer.id'))

# Create the DB
db.create_all()

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# Create the API endpoints from the DB Models
# These will be available at /api/<tablename>
manager.create_api(Beer, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(Type, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(Review, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(Reviewer, methods=['GET', 'POST', 'PUT', 'DELETE'])

# start the flask app
app.run(debug=True)
