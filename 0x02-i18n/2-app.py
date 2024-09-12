#!/usr/bin/env python3
"""A Basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """A language class representation"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale() -> str:
    """get the web page locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def home() -> str:
    """The home route"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
