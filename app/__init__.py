import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from app import views, models