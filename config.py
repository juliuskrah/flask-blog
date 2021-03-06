import os

basedir = os.path.abspath(os.path.dirname(__file__))

'''
Uncomment the line below to enable sqlite db
'''
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/app'
'''
Uncomment the line below to enable sqlite db
'''
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_ENABLED = True
SECRET_KEY = 'somesecretkey'

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['you@example.com']
