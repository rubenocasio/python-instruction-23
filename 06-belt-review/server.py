from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import jokes
from flask_app.controllers import groans

if __name__ == "__main__":
    app.run(debug = True)