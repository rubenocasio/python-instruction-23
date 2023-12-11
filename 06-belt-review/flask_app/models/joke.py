from flask import flash
from pprint import pprint
from flask_app.models import user
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "belt_exam_db"

class Joke:
    def __init__(self, data):
        self.id = data["id"]
        self.setup = data["setup"]
        self.punchline = data["punchline"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None

    @staticmethod
    def form_is_valid(form_data):
        is_valid = True # we assume this is true
        #This is first name
        if len(form_data['setup']) < 3:
            flash("Setup line is invalid and needs to be 3 characters or more.", 'joke')
            is_valid = False
        #This is last name
        if len(form_data['punchline']) < 3:
            flash("Setup line is invalid and needs to be 3 characters or more.", 'joke')
            is_valid = False
        return is_valid
    
    @classmethod
    def create(cls, form_data):
        query = """
        INSERT into jokes (setup, punchline, created_at, updated_at, user_id)
        VALUES (%(setup)s, %(punchline)s, NOW(), NOW(), %(user_id)s );
        """
        joke_id = connectToMySQL(DATABASE).query_db(query, form_data)
        return joke_id
    
    @classmethod
    def get_all_jokes_with_users(cls):
        query = "SELECT * FROM jokes JOIN users ON jokes.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)

        jokes = []
        pprint(results)
        for result in results:
            joke = Joke(result)
            creator = user.User.get_by_id(result["user_id"])
            joke.user = creator
            jokes.append(joke)
        return jokes
    
    @classmethod
    def get_one_with_user(cls, joke_id):
        query = "SELECT * FROM jokes JOIN users ON jokes.user_id = users.id WHERE jokes.id = %(joke_id)s;"
        data = {"joke_id" : joke_id}
        results = connectToMySQL(DATABASE).query_db(query, data)
        joke = Joke(results[0])
        creator = user.User.get_by_id(results[0]["user_id"])
        joke.user = creator
        return joke
    
    @classmethod
    def update(cls, form_data):
        query = "UPDATE jokes SET setup = %(setup)s, punchline = %(punchline)s WHERE id = %(joke_id)s"
        connectToMySQL(DATABASE).query_db(query, form_data)
        return
    
    @classmethod
    def delete(cls, joke_id):
        query = "DELETE FROM jokes WHERE id = %(joke_id)s"
        data = {"joke_id" : joke_id}
        connectToMySQL(DATABASE).query_db(query, data)
        return