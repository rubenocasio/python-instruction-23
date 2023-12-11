from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

DATABASE = 'loginregistration_db'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        data = {'id' : id}

        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * from users"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @staticmethod
    def validate_registration(data):
        is_valid = True # we assume this is true
        #This is first name
        if len(data['first_name']) < 3:
            flash("First name must be at least 3 characters.", 'register')
            is_valid = False
        #This is last name
        if len(data['last_name']) < 3:
            flash("Last name must be at least 3 characters.", 'register')
            is_valid = False
        #This is email
        if len(data['email']) == 0:
            flash("Email address is required", 'register')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']):
            flash("Email address is required", 'register')
            is_valid = False
        else:
            existing_user = User.get_by_email({'email' : data['email']})
            if existing_user:
                flash("Email address is already in use!", 'register')
                is_valid = False
        #This is password
        if len(data['password']) < 8:
            flash("Password should be more than 8 characters!", 'register')
            is_valid = False
        if data['password'] != data['confirm']:
            flash("Passwords should match", 'register')
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True

        user_in_db = User.get_by_email({'email' : data['email']})
        if not user_in_db:
            flash("Email not found", 'login')
            return False
        if not bcrypt.check_password_hash(user_in_db.password, data['password']):
            flash("Incorrect password fool!HAHAHAH Try again", 'login')
            return False
        return is_valid