from flask import Flask, render_template

page = Flask(__name__)

@page.route("/")
def hello_world():
    return render_template('text.html')