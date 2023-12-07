from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.song import song

DATABASE = "albums_db"

class Album:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.artist = data["artist"]
        self.genre = data["genre"]
        self.is_owned = data["is_owned"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.songs = []
    
    @classmethod
    def create(cls, data):
        query = """
        Insert INTO albums (title, artist, genre, is_owned,created_at,updated_at)
         VALUES (%(title)s, %(artist)s, %(genre)s, %(is_owned)s, NOW(), NOW());
         """
        album_id = connectToMySQL(DATABASE).query_db(query,data)
        return album_id