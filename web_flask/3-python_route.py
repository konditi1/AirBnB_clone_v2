#!/usr/bin/python3
""" import Flask from web_flask/__init__.py """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """print("Hello HBNB!")"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """print("HBNB")"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """print("C ")"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """print("Python ")"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
