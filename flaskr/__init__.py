from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
#from flask_bootstrap import Bootstrap
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


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))