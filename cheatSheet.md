1. mkdir dojosurvey
2. cd dojosurvey
3. pipenv shell
4. pipenv install PyMySQL flask
5. make server.py file
6. server.py contents:
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == "__main__":
    app.run(debug=True)
7. python server.py
8. mkdir templates
9. create index.html
10. text an h1 rendering at "/"
