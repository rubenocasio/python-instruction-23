# 1. mkdir post-session-demo
# 2. cd post-session-demo
# 3. pip install pipenv (One time install)
# 4. pipenv shell (Virtual Environment)
# 5. pipenv install flask (whats in your env run: pip list)
# 6. python server.py

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "You can name this anything"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print(request.form)

    session['account'] = request.form['account']
    session['name'] = request.form['name']
    return redirect('/display')

@app.route('/display')
def display():
    print("This is my display route")
    
    # if 'account' in session:
    #     account = session['account']
    # else:
    #     account = 'Nothing here to look at'
    # return render_template('display.html', account = account)
    return render_template('display.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)   