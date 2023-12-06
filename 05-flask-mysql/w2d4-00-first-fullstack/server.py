from flask import Flask, render_template, redirect, request, session
from pprint import pprint
app = Flask(__name__)

from friend import Friend

# The "@" decorator associates this route with the function immediately following
@app.route('/')
def index():
    friends = Friend.get_all()

    print(friends[0].first_name)

    return render_template('index.html', friends = friends)

## MORE ROUTES Below 

@app.route("/friends/new")
def new_friend():
    return render_template("new.html")


if __name__ == "__main__":
    app.run(debug=True)