from flask import Flask, render_template
app = Flask(__name__)


#@app.route('/')
#def homepage():
 #   return "<h1>WELCOME TO OUR BLOG APP<h1>"

@app.route('/')
def index():
    first_name = "mide"
    stuff = "This is a <strong> bold </strong> text"
    
    favorite_pizza = ["Pepperoni", "cheese", "Mushrooms", 41]
    return render_template("index.html", first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name = name)

#create custom error page
#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
