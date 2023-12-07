# ...server.py
from flask_app import app

import flask_app.controllers.albums
import flask_app.controllers.songs

if __name__ == "__main__":
    app.run(debug=True, port=5001)