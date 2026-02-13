# the "from" imports libraries and functions we need. In this case we are importing Flask and some helper functions from the flask library.
from flask import Flask, request, render_template, send_from_directory

# Create an instance of the Flask class. This instance will be our WSGI application.
app = Flask(__name__)

# The route() decorator tells Flask what URL should trigger our function. In this case, we are defining the root URL ("/").
@app.route("/")
def home():
    return "<h1>Hello from the server!</h1>Try the following routes:<br><ul><li><a href='/greet?name=YourName'>/greet?name=YourName</a></li><li><a href='/status'>/status</a></li><li><a href='/name.html'>/name.html</a></li><li><a href='/practice'>/practice</a></li></ul>"

# When users visit /greet, the greet function will be called and the name parameter will be read from the URL query string and used to generate a personalized greeting.
@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    return f"<h1>Hello, {name}!</h1>"

# Here is an example using a template with dynamic content. The render_template function renders an HTML file named status.html located
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

# This route will be for your own practice. It will read query parameters for name, role, a, b, and op.
# Name and role should have default values (e.g., "Student" and "MSHI"). a and b should default to 0, and be converted to floats.
# Op should contain describe the mathematical operation (add, sub(tract), mul(tiply), div(ide)) to perform
# The route should compute the result of applying the operation to a and b, and return a clear response that includes the inputs and the result.
@app.route("/practice")
def practice():
    # TODO 1: Read query params with defaults
    
    # TODO 2: Read a and b, default to 0, and convert to float. If conversion fails, return an error message.

    # TODO 3: Compute result based on op

    # TODO 4: Return a clear response
    return "This is a placeholder response. Replace this with your actual implementation."

if __name__ == "__main__":
    app.run(debug=True)