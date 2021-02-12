from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
# from flask_bootstrap import Bootstrap
#from flaskr.models.todo import *
from markupsafe import escape

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/test')
def test():
    return 'Hello Beeyotches'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
def index():
    if 'username' in session:
        todo_list = Todo.query.all()
        print(todo_list)
        return render_template('index.html')
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return '{}\'s profile'.format(escape(username))


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post%d' % post_id


@app.route('/path/<path:subpath>', methods=['GET'])
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)
    # return jsonify(name='bria', id=90, email=128)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    db.create_all()

    app.run(debug=True)
