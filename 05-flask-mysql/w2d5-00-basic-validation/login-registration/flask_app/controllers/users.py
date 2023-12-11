from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)

from flask_app.models.user import User

@app.route('/')
def index():
    print('Im HOME')
    return render_template('index.html')

# @app.route('/register/user', methods=['POST'])
@app.post('/register/user')
def register():
    # validate the form here ...
    if not User.validate_registration(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/dashboard")

@app.post('/login')
def login():
    # validate the form here ...
    if not User.validate_login(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    user_in_db = User.get_by_email({'email' : request.form['email']})
    session['user_id'] = user_in_db.id
    return redirect("dashboard")

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        users = User.get_all()
        return render_template('dashboard.html', users = users)
    return redirect('/')

@app.post('/logout')
def logout():
    if 'user_id' in session:
        # session.pop('user_id', None)
        session.clear()
    return redirect('/')