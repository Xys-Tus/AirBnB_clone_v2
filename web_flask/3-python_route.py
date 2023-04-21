#!/usr/bin/python3
"""
Working with Flask
displays a defualt if nothing is provided
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def to_hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def to_nextpage(text):
    """returns HBNB"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/(<text>)', strict_slashes=False)
def to_python_text(text):
    """returns Python is cool if nothing is passed
        else return python followed by the world that was passed
    """
    if text == "" or text == " ":
        return 'Python is cool'
    else:
        return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
