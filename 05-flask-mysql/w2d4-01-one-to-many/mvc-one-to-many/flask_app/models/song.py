from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.album import album

DATABASE = "albums_db"

class Song:
    def __init__(self, data):
        self.id = data["id"]
        self.number = data["number"]
        self.title = data["title"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.album_id = data["album_id"]

    @classmethod
    def get_one(cls, song_id):
        query = "SELECT * FROM songs WHERE id = %(song_id)s;"
        data = {"song_id" : song_id}
        results = connectToMySQL(DATABASE).query_db(query, data)
        song = Song(results[0])
        return song