from flask import Flask

page = Flask(__name__)

@page.route("/")
def pong(text):
    return "<p>{}</p>".format(text)