"""
1-hbnb_route.py - Flask web application with additional route.

This script starts a Flask web application listening on 0.0.0.0, port 5000.
It defines routes '/' and '/hbnb' with the option strict_slashes=False.

Usage: python3 1-hbnb_route.py
"""

from flask import Flask

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

if __name__ == '__main__':
    """
    Run the Flask application on 0.0.0.0, port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
