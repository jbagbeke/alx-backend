#!/usr/bin/env python3
"""
Basic Flask setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Babel Config Class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

babel = Babel(app, config=Config)


@app.route('/')
def root_func() -> str:
    """
    Basic flask app root
    """
    return render_template('0-index.html')
