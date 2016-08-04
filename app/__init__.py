from flask import Flask


app = Flask(__name__)
app.config.from_object('config')


from app import views  # avoids circular import errors when put at the end 'cos the `views` also import `app`

