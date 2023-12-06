# checklist

- [x] create a new directory
- [ ] inside the directory create virtural env by running:

```bash
[python -m] pipenv install flask
```

- [ ] activate the virtual env every time you open a new terminal:

```bash
[python -m] pipenv shell 
```

- [ ] create [server.py](server.py)

```py
from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

## MORE ROUTES HERE 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
```

- [ ] start application by running:

```
python server.py
```

- [ ] go to [localhost:5000](http://localhost:5000/)

- [ ] create a [templates](templates/index.html) folder that contains our HTML
<!-- 1. mkdir dojosurvey
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
10. text an h1 rendering at "/" -->
