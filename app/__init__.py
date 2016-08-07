import os
from flask import Flask
from flask_login import LoginManager
from flask_openid import OpenID
from flask_sqlalchemy import SQLAlchemy
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

""" avoids circular import errors when put at the end 'cos the `views` also import `app` """
from app import views, models

