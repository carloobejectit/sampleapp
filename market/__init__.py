from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
#added security layer
app.config['SECRET_KEY'] = 'a84290384b57e81c601c0e87'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes