# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

DATABASE = "friends_db"
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends
            
#Create route
    @classmethod
    def create(cls, form_data):
        query = """
        INSERT INTO friends (first_name, last_name, occupation) 
        VALUES (%(first_name)s, %(last_name)s, %(occupation)s);
        """
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query, form_data)
        return results

#Details route & Edit route (view only)
    @classmethod
    def get_one(cls, friend_id):
        query = "SELECT * FROM friends WHERE id = %(friend_id)s;"
        data = {"friend_id" : friend_id}
        results = connectToMySQL(DATABASE).query_db(query, data)
        friend =  Friend(results[0])
        return friend

#Update route
    @classmethod
    def update(cls, form_data):
        query = """
        UPDATE friends SET first_name = %(first_name)s, last_name = %(last_name)s, occupation = %(occupation)s 
        WHERE id = %(friend_id)s;
        """
        # make sure to call the connectToMySQL function with the schema you are targeting.
        # results = connectToMySQL(DATABASE).query_db(query, form_data)
        # return results
        connectToMySQL(DATABASE).query_db(query, form_data)

#Delete route
    @classmethod
    def delete(cls, friend_id):
        query = "DELETE FROM friends WHERE id = %(friend_id)s;"
        data = {"friend_id" : friend_id}
        connectToMySQL(DATABASE).query_db(query, data)
        return