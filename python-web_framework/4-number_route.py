"""
4-number_route.py - Flask web application with additional routes.

This script starts a Flask web application listening on 0.0.0.0, port 5000.
It defines routes '/', '/hbnb', '/c/<text>', '/python/<text>', and '/number/<n>' with the option strict_slashes=False.

Usage: python3 4-number_route.py
"""

from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route to display 'Hello HBNB!'

    Returns:
        str: The greeting message.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route to display 'HBNB'

    Returns:
        str: The message 'HBNB'.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route to display 'C ' followed by the value of the text variable.

    Args:
        text (str): The text variable.

    Returns:
        str: The formatted message.
    """
    return "C {}".format(escape(text.replace('_', ' ')))

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
def python_text(text):
    """
    Route to display 'Python ' followed by the value of the text variable.
    The default value of text is 'is cool'.

    Args:
        text (str): The text variable.

    Returns:
        str: The formatted message.
    """
    return "Python {}".format(escape(text.replace('_', ' ')))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route to display 'n is a number' only if n is an integer.

    Args:
        n (int): The number.

    Returns:
        str: The formatted message or a 404 error if n is not an integer.
    """
    return "{} is a number".format(n)

if __name__ == '__main__':
    """
    Run the Flask application on 0.0.0.0, port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
