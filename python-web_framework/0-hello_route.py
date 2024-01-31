"""
0-hello_route.py - A simple Flask web application.

This script starts a Flask web application listening on 0.0.0.0, port 5000.
It defines a route '/' with the option strict_slashes=False, displaying 'Hello HBNB!'.

Usage: python3 0-hello_route.py
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

if __name__ == '__main__':
    """
    Run the Flask application on 0.0.0.0, port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
