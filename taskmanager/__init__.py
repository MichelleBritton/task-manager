import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa

# Create an instance of the imported Flask() class and store in a variable
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Create an instance of the SQLAlchemy class which will be assigned to a variable and set to the instance of our Flask app
db = SQLAlchemy(app)

from taskmanager import routes  # noqa
