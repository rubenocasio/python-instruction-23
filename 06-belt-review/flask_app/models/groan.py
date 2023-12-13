from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from pprint import pprint
from flask import flash

DATABASE = "belt_exam_db"

class Groan:
    def __init__(self, data):
        self.user_id = data["user_id"]
        self.joke_id = data["joke_id"]
    
    @classmethod
    def create(cls, form_data):
        query = "INSERT INTO groans (user_id, joke_id) VALUES (%(user_id)s, %(joke_id)s);"
        groan_id = connectToMySQL(DATABASE).query_db(query, form_data)
        return groan_id

    @classmethod
    def get_groan_count(cls, joke_id):
        query = "SELECT COUNT(joke_id) as 'count' FROM groans WHERE joke_id = %(joke_id)s;"
        data = {"joke_id" : joke_id}
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results[0]["count"]
    
    @classmethod
    def get_all_by_joke_id(cls, joke_id):
        query = "SELECT * from groans WHERE joke_id = %(joke_id)s;"
        data = {"joke_id" : joke_id}
        results = connectToMySQL(DATABASE).query_db(query, data)
        groans = []

        for result in results:
            groan = Groan(result)
            groans.append(groan)
        return groans