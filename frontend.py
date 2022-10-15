from flask import Flask

page = Flask(__name__)

@page.route("/")
def hello_world():
    return "<p>Hello, World!</p>"