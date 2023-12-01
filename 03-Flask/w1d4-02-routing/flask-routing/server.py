# Import Flask to allow us to create our app
from flask import Flask, render_template

# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# The "@" decorator associates this route with the function immediately following
# '/' means root
@app.route('/')
def index():
    # Return the string 'Hello World!' as a response
    return 'Hello World!'

@app.route('/home/<name>')
def greet_name(name):
    # Return the string 'Hello World!' as a response
    return f'<h1>Hello, {name} Welcome to Flask <h1>'

@app.route('/home/index')
def home():
    return render_template('index.html')

@app.route('/home/students')
def students():
    students = [
        {'name': 'Kyle', 'age': 21},
        {'name': 'Kevin', 'age': 21},
        {'name': 'Brooks', 'age': 21},
    ]
    name = 'Ruben'
    return render_template('students.html', some_name = name, students = students )

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error = error)

# Ensure this file is being run directly and not from a different module    
if __name__=="__main__":
    # Run the app in debug mode.
    app.run(debug=True)