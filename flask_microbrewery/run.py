from flask.ext.restless import APIManager
from flask_microbrewrey.app.models import Beer
from app import app, db

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Beer, methods=['GET', 'POST', 'DELETE'])

# start the flask app
app.run(debug=True)
