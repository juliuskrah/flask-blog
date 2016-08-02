from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Julius'}  # username
    posts = [
        {
            'author': {'nickname': 'John'},
            'post': 'This movie is awesome'
        },
        {
            'author': {'nickname': 'Mary'},
            'post': 'The match was a draw'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
