![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)

# Basic To-Do App

A simple To-Do app powered by Flask and performs CRUD operations using SQLAlchemy.

For styling [semantic-ui](https://semantic-ui.com/) is used.

## Dependencies

You will need to install [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/#installation) following the installation instructions in the documentation.

### Setup
Create project with virtual environment

```console
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

Activate it (I used Windows)
```console
venv\Scripts\activate
```

Install Flask and SQLAlchemy
```console
$ pip install Flask
$ pip install Flask-SQLAlchemy
```

Set environment variables in terminal (Windows)
```console
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```

Run the app
```console
$ flask run
```

