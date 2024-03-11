# Importing the Flask class from the flask module
from flask import Flask

# Creating an instance of the Flask class and assigning it to the variable 'app'
app = Flask(__name__)

# Creating a route decorator for the root URL ('/') that calls the hello_world function when accessed
@app.route('/')
def hello_world():
    # Returning a string as the response when the root URL is accessed
    return "Hello, Simple Flask application"

# Conditional check to ensure that the app is being run directly
if __name__ == "__main__":
    # Running the Flask application
    app.run()