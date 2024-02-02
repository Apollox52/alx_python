from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route for the root URL.
    
    Returns:
        str: Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Route for /hbnb URL.
    
    Returns:
        str: HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Route for /c/<text> URL.
    
    Args:
        text (str): Text parameter.
    
    Returns:
        str: C followed by the formatted text.
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python(text='is cool'):
    """Route for /python/<text> and /python/ URLs.
    
    Args:
        text (str, optional): Text parameter. Defaults to 'is cool'.
    
    Returns:
        str: Python followed by the formatted text.
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Route for /number/<n> URL.
    
    Args:
        n (int): Integer parameter.
    
    Returns:
        str: n is a number.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Route for /number_template/<n> URL.
    
    Args:
        n (int): Integer parameter.
    
    Returns:
        render_template: HTML template with the number.
    """
    return render_template('5-number_template.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
