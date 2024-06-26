#!/usr/bin/env python3
"""
Basic Flask setup
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError


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

    locale = g.user

    if locale:
        return g.user.get("locale")

    locale = request.accept_languages.best_match(app.config['LANGUAGES'])

    if locale:
        return locale

    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """
    Time zone selector
    """
    try:
        tzname = request.headers.get('X-Timezone')
        if tzname:
            return pytz.timezone(tzname)
    except UnknownTimeZoneError:
        pass


def get_user(login_as):
    """
    Mock user login system
    """
    if not login_as:
        return None

    user = users.get(int(login_as), None)
    return user


@app.before_request
def before_request():
    """
    Before request function
    """
    login_as = request.args.get('login_as', None)

    if login_as:
        user = get_user(login_as)
        g.user = user


@app.route('/')
def root_func() -> str:
    """
    Basic flask app root
    """
    return render_template('5-index.html')
