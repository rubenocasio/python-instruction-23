from flask_app.models.groan import Groan
from flask import redirect, request
from flask_app import app

@app.post("/groans/create")
def create_groan():
    Groan.create(request.form)
    return redirect("/jokes")