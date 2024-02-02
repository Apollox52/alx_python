from flask import Flask, render_template

app = Flask(__name__)

# Route for the root URL
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' on the root URL."""
    return 'Hello HBNB!'

# Route for /hbnb URL
@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display 'HBNB' on the /hbnb URL."""
    return 'HBNB'

# Route for /c/<text> URL
@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Display 'C ' followed by the formatted text on /c/<text> URL.
    
    Args:
        text (str): Text parameter.
    """
    return 'C {}'.format(text.replace('_', ' '))

# Route for /python/<text> and /python/ URLs
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python(text='is cool'):
    """Display 'Python ' followed by the formatted text on /python/<text> and /python/ URLs.
    
    Args:
        text (str, optional): Text parameter. Defaults to 'is cool'.
    """
    return 'Python {}'.format(text.replace('_', ' '))

# Route for /number/<n> URL
@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Display 'n is a number' on /number/<n> URL.
    
    Args:
        n (int): Integer parameter.
    """
    return '{} is a number'.format(n)

# Route for /number_template/<n> URL
@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Render an HTML template with the number on /number_template/<n> URL.
    
    Args:
        n (int): Integer parameter.
    """
    return render_template('5-number_template.html', number=n)

# Run the Flask app on 0.0.0.0:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
