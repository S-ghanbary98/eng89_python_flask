# Creating a file called app.py
# Lets see how we can use Flask to interact with the browser.
# Install Flask via `pip install flask`






from flask import Flask, redirect, url_for, render_template
# We have to create an object of this class

app = Flask(__name__)  # initalizing an app instance.


# Let's create a function to link to our home/default page
# Lets connect this function to our browser.

@app.route("/")  # Decorating our function with @app.route to set our route

def index():
    return "Welcome to Engineering 89 DevOps Team"


@app.route("/welcome/")
def welcome():
    return render_template("welcome.html")


# Creating a decorator to route traffic.


@app.route("/login/")

def login():   # redirect and url_for to redirect pages.
    # return "<h1> Hello World !!!!!!!! </h1> <h2> Shervin Wrote this</h2>"
    return redirect(url_for("welcome"))       ## This will redirect user to the welcome page


if __name__ == "__main__":
    app.run(debug=True)


# Let's add our HTML file to reirect away from python flask to .html file.
# Project folder
 #template folder
    # welcome.html
# app.py

# What if the page is not available?? 404 error given. But we can also control it amd redirect users