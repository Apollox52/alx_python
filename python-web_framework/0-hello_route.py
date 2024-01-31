# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class, representing the web application
app = Flask(__name__)

# Define a route for the root URL ("/") with strict_slashes=False option
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ("/").
    
    Returns:
        str: A string "Hello HBNB!"
    """
    return 'Hello HBNB!'

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Start the Flask development server on 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
