from flask_wtf import Form
from wtforms import StringField, BooleanField, validators


class LoginForm(Form):
    openid = StringField('openid', [validators.DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
