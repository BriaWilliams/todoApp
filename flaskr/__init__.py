from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
# from flask_bootstrap import Bootstrap
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Meeyotches?'


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


@app.route('/path/<path:subpath>', methods=['GET'])
def show_subpath(subpath):
    # return 'Subpath %s' % escape(subpath)
    return jsonify(name='bria', id=90, email=128)


@app.route('/projects/')
def projects():
    return 'The projectgyuyg2 page'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run(debug = True)
