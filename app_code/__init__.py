import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'garbage'
db = SQLAlchemy(app)
