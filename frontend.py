from flask import Flask

class FrontEnd():

    flask = Flask(__name__)

    @flask.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"