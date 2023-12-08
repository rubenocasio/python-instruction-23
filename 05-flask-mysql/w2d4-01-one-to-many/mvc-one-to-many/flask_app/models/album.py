from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.song import Song

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
    
    #Read All
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM albums"
        results = connectToMySQL(DATABASE).query_db(query)
        albums = []
        for album in results:
            albums.append(cls(album))
        return albums
    
    #Read One (Join Relationship)
    @classmethod
    def get_albums_with_songs(cls, album_id):
        query = """
        SELECT * FROM albums
        LEFT JOIN songs
        ON songs.album_id = albums.id WHERE albums.id = %(album_id)s;
        """
        data = {"album_id" : album_id}
        results = connectToMySQL(DATABASE).query_db(query,data)

        album = Album(results[0])

        for result in results:
            if result["songs.id"]:
                song = Song.get_one(result["songs.id"])
                album.songs.append(song)
        return album

    #Update
    @classmethod
    def update(cls, album_id, form_data):
        query = """
        UPDATE albums SET title = %(title)s, artist = %(artist)s, 
        genre = %(genre)s, is_owned = %(is_owned)s WHERE id = %(album_id)s;
        """
        connectToMySQL(DATABASE).query_db(query, form_data)
        return
    
    #Delete
    @classmethod
    def delete(cls, album_id):
        query = "DELETE FROM albums WHERE id = %(album_id)s;"
        data = { "album_id": album_id }
        connectToMySQL(DATABASE).query_db(query, data )
        return