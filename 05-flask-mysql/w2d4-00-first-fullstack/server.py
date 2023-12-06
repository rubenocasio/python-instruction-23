from flask import Flask, render_template, redirect, request, session
from pprint import pprint
app = Flask(__name__)

from friend import Friend

# The "@" decorator associates this route with the function immediately following
@app.route('/')
def index():
    friends = Friend.get_all()
    pprint(friends[0].first_name)
    return render_template('index.html', friends = friends)

## MORE ROUTES Below 

# View route to open new form page
@app.route("/friends/new")
def new_friend():
    return render_template("new.html")

#Create route
@app.post("/friends/create")
def create_friend():
    friends = Friend.create(request.form)
    return redirect("/")

#Details route
@app.route("/friends/<int:friend_id>")
def friend_details(friend_id):
    friend = Friend.get_one(friend_id)
    return render_template("details.html", friend = friend)

#Edit route (view only)
@app.route("/friends/<int:friend_id>/edit")
def edit_friend(friend_id):
    friend = Friend.get_one(friend_id)
    return render_template("edit.html", friend = friend)

#Update route
@app.post("/friends/<int:friend_id>/update")
def update_friend(friend_id):
    Friend.update(request.form)
    return redirect(f"/friends/{friend_id}")

#Delete route
@app.post("/friends/<int:friend_id>/delete")
def delete_friend(friend_id):
    Friend.delete(friend_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)