# Import Flask to allow us to create our app
from flask import Flask

# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# The "@" decorator associates this route with the function immediately following
# / means root
@app.route('/')
def index():
    # Return the string 'Hello World!' as a response
    return 'Hello World!'

@app.route('/<name>')
def greet_name(name):
    # Return the string 'Hello World!' as a response
    return f'<h1>Hello, {name} Welcome to Flask <h1>'

# Ensure this file is being run directly and not from a different module    
if __name__=="__main__":
    # Run the app in debug mode.
    app.run(debug=True)