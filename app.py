# the "from" imports libraries and functions we need. In this case we are importing Flask and some helper functions from the flask library.
from flask import Flask, request, render_template, send_from_directory

# Create an instance of the Flask class. This instance will be our WSGI application.
app = Flask(__name__)

# The route() decorator tells Flask what URL should trigger our function. In this case, we are defining the root URL ("/").
@app.route("/")
def home():
    return "<h1>Hello from the server!</h1>"

# When users visit /greet, the greet function will be called and the name parameter will be read from the URL query string and used to generate a personalized greeting.
@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    return f"<h1>Hello, {name}!</h1>"

# Here is an example of using a template with dynamic content. The render_template function renders an HTML file named status.html located
# in the templates directory. This HTML file has a placeholder for the "status" variable that we pass to it.
# Open the templates/status.html file to see how the variable is used.
@app.route("/status")
def status():
    system_status = "All systems operational"
    return render_template("status.html", status=system_status)

# This route serves a static HTML file named name.html located in the static directory. Flask does not perform any processing on static files; it simply serves them as they are.
@app.route("/name.html")
def name():
    return send_from_directory("static", "name.html")

# This route handles form submissions. It expects a POST request with a form field named "username".
@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    return render_template("result.html", name=username)

if __name__ == "__main__":
    app.run(debug=True)