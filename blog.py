from flask import Flask
app = Flask(__name__)


@app.route('/')
def homepage():
    return "<h1>WELCOME TO OUR BLOG APP<h1><br><br>"