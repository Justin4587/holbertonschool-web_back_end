#!/usr/bin/env python3
""" flask module """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ config the tower of babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ localization best match selector """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """ render html page """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
