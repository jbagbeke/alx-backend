#!/usr/bin/env python3
"""
Basic Flask setup
With Babel implementations
"""
from flask import Flask, render_template, request
from flask import g
from flask_babel import Babel


class Config:
    """
    Babel Config Class
    With config variable declarations
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """
    Babel Locale Selector
    based on best matched langauge setting specified
    in header
    """
    locale = request.args.get('locale', None)
    if locale:
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Mock user login system
    with users acting as temporary db
    """
    login_as = request.args.get('login_as', None)

    if not login_as:
        return None

    user = users.get(int(login_as), None)
    return user


@app.before_request
def before_request() -> None:
    """
    Before request function
    Runs before actual request
    """
    user = get_user()
    g.user = user


@app.route('/')
def root_func() -> str:
    """
    Basic flask app root handler
    renders simple html file
    """
    return render_template('5-index.html')
