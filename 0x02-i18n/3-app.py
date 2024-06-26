#!/usr/bin/env python3
"""
Basic Flask setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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


@babel.localeselector
def get_locale() -> str:
    """
    Babel Locale Selector
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def root_func() -> str:
    """
    Basic flask app root
    """
    return render_template('3-index.html')
