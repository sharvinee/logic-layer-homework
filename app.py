# the "from" imports libraries and functions we need. In this case we are importing Flask and some helper functions from the flask library.
from flask import Flask, request, render_template, send_from_directory

# Create an instance of the Flask class. This instance will be our WSGI application.
app = Flask(__name__)

# The route() decorator tells Flask what URL should trigger our function. In this case, we are defining the root URL ("/").
@app.route("/")
def home():
    return "<h1>Welcome to the Logic Layer practice app!</h1>Try the following routes:<br><ul><li><a href='/greet?name=YourName'>/greet?name=YourName</a></li><li><a href='/status'>/status</a></li><li><a href='/name.html'>/name.html</a></li><li><a href='/practice'>/practice</a></li></ul>"

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
    environment = "Development"
    return render_template("status.html", status=system_status, environment=environment)

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
    name = request.args.get("name", "Student")
    role = request.args.get("role", "MSHI")
    op = request.args.get("op", "add").lower()

    # TODO 2: Read a and b, default to 0, and convert to float. If conversion fails, return an error message.
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
    except ValueError:
        return "Invalid input: a and b must be numbers.", 400

    # TODO 3: Compute result based on op
    if op in ["add", "+"]:
        result = a + b
        operation_name = "addition"
    elif op in ["sub", "subtract", "-"]:
        result = a - b
        operation_name = "subtraction"
    elif op in ["mul", "multiply", "*"]:
        result = a * b
        operation_name = "multiplication"
    elif op in ["div", "divide", "/"]:
        if b == 0:
            return "Invalid operation: division by zero is not allowed.", 400
        result = a / b
        operation_name = "division"
    else:
        return "Invalid op. Use add, sub, mul, or div.", 400

    # TODO 4: Return a clear response
    return (
        f"<h1>Practice Result!</h1>"
        f"<p>Name: {name}</p>"
        f"<p>Role: {role}</p>"
        f"<p>Operation: {operation_name}</p>"
        f"<p>Inputs: a={a}, b={b}</p>"
        f"<p>Result: {result}</p>"
    )

if __name__ == "__main__":
    app.run(debug=True)