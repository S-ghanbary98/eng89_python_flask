# Model View Controller (MVC) with Python Flask



## Python Flask

- Flask is a python micro-framework.
- Flask is used to develop web apps.


### Installing and importing Flask
- We must first install the module using `pip install flask` at which point we import it on our `app.py` document.
- Then we initialize the app instance.
```python
from flask import Flask, redirect, url_for, render_template
# We have to create an object of this class

app = Flask(__name__)  # initalizing an app instance.
```

### Routing Python to browser

- We route the following text in the `index` function so it display in the browser as follows.
```python
@app.route("/")  # Decorating our function with @app.route to set our route
def index():
    return "Welcome to Engineering 89 DevOps Team"
```
### Running the Program
- We can run the program by typing `flask run`

### Redirecting URL
- we redirect to another url using the command