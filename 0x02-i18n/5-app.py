#!/usr/bin/env python3
"""
Basic Flask setup
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Dict, Union


class Config:
    """
    Babel Config Class
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
    """
    locale = request.args.get('locale', None)
    if locale:
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(login_as) -> Union[Dict, None]:
    """
    Mock user login system
    """
    user = users.get(int(login_as), None)
    return user


@app.before_request
def before_request() -> None:
    """
    Before request function
    """
    login_as = request.args.get('login_as', None)

    user = get_user(login_as)
    g.user = user


@app.route('/')
def root_func() -> str:
    """
    Basic flask app root
    """
    return render_template('5-index.html')
