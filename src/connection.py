from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import and_

stringConnection = 'mysql+pymysql://root@localhost/basebiblioteca'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = stringConnection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)