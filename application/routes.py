from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True )

@app.route("/home")
def home():
    return render_template("home.html", index=True )
