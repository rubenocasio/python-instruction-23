from flask import Flask, render_template, session, redirect
app = Flask(__name__)

app.secret_key = "It can be whatever you want it to be or not to be"

@app.route('/')
def index():
    if not 'counter' in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    if 'counter' not in session:
        session['counter'] = 2
    else:
        session['counter'] += 1
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)