#!/usr/bin/env python3
"""
Basic Flask setup
"""
from flask import Flask, render_template
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


@app.route('/')
def root_func() -> str:
    """
    Basic flask app root
    """
    return render_template('0-index.html')
