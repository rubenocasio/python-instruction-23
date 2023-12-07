from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.album import Album


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/album/new")
def new_album():
	return render_template("new.html")

@app.route('/create/album', methods=['POST'])
def create_album():
	data = {
        	"title" : request.form['title'],
        	"artist" : request.form['artist'],
        	"genre" : request.form['genre'],
        	"is_owned" : request.form.get('is_owned')
	}
	Album.create(data)
	print(data)
	return redirect('/')

