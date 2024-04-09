#!/usr/bin/env python3
"""
Basic Flask setup
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root_func() -> str:
    """
    Basic flask app root
    """
    return render_template('0-index.html')
