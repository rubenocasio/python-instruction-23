from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.joke import Joke


# @app.route("/jokes")
@app.get("/jokes")
def all_jokes():
    if "user_id" not in session or session["user_id"] == False:
        return redirect("/")
    user = User.get_by_id(session["user_id"])
    jokes = Joke.get_all_jokes_with_users()
    return render_template("all_jokes.html", user = user, jokes = jokes)

@app.get("/joke/new")
def new_joke():
    if "user_id" not in session:
        return redirect("/")
    user = User.get_by_id(session["user_id"])
    return render_template("new.html", user = user)

@app.post("/joke/create")
def create_joke():
    if "user_id" not in session:
        return redirect("/")
    if not Joke.form_is_valid(request.form):
        return redirect("/joke/new")
    Joke.create(request.form)
    return redirect("/jokes")
