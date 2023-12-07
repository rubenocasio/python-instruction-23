from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.album import album

DATABASE = "albums"

class Song:
    def __init__(self, data):
        self.id = data["id"]
        self.number = data["number"]
        self.title = data["title"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.album_id = data["album_id"]

    