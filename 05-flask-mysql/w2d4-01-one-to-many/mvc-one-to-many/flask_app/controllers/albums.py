from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.album import Album

@app.route("/")
def index():
	albums = Album.get_all()
	return render_template("index.html", albums = albums)

@app.route("/album/new")
def new_album():
	return render_template("new.html")

@app.route('/create/album', methods=['POST'])
def create_album():
	data = {
        	"title" : request.form['title'],
        	"artist" : request.form['artist'],
        	"genre" : request.form['genre'],
        	"is_owned": 'is_owned' in request.form #This is new
	}
	Album.create(data)
	print(data)
	return redirect('/')

@app.route("/album/<int:album_id>")
def album_details(album_id):
	album = Album.get_albums_with_songs(album_id)
	return render_template("details.html", album = album)


@app.route("/album/<int:album_id>/edit")
def edit_album(album_id):
	album = Album.get_albums_with_songs(album_id)
	return render_template("edit.html", album = album)


@app.route("/album/<int:album_id>/update", methods=["POST"])
def update_album(album_id):
	 #This is new
	form_data = request.form.to_dict()
	form_data['is_owned'] = 'is_owned' in request.form
	Album.update(album_id, form_data)
	return redirect("/")

@app.route("/album/<int:album_id>/delete", methods=["POST"])
def delete_album(album_id):
	#delete method
	Album.delete(album_id)
	return redirect("/")