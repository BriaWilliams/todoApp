from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
# from flask_bootstrap import Bootstrap
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Mitches'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return '{}\'s profile'.format(escape(username))


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post%d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
