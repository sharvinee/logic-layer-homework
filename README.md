# The Logic Layer
## Using Flask to demonstrate server-side processes

## Overview
This Flask application demonstrates how to deliver dynamic content to users by processing data on the server and returning customized responses. Students will learn how different Flask routes handle data in different ways.

---
## How to Run
In the TERMINAL prompt below, enter the following commands and then press `<Enter>`

```bash
python app.py
```

You will see a message in the bottom right: "Your application is available on port 5000" Click the "Open in browser" button to open the web app and explore each route.

If this does not work, click on the PORTS tab in your Codespaces environment and then follow the link to open in your browser.

## Routes & Learning Objectives
### What is a route?
A Flask route is a rule that tells the server:


“When a request comes in for this URL, run this Python function and send back its result.”

They are defined by an `@app.route()` decorator. Whatever is inbetween the `( )` is the URL that the route hooks to.

---
### Exploring Routes
In Codespaces, open the `app.py` file to see how routes are built in Flask. Refer back and forth between this README and `app.py` to explore.

---
#### Route 1: `@app.route("/")`
**Function:** `home()`

**What it does:**
- Returns a simple static HTML `<h1>` heading when users visit the root URL (`/`)
- This is the most basic Flask route—it returns the same response every time

**Learning point:**
- This is static content. The server always returns `<h1>Hello from the server!</h1>` regardless of user input
- When your browser opens, you will automatically be looking at the `/` route

---

#### Route 2: `@app.route("/greet")`
**Function:** `greet()`

**What it does:**
- Accepts a URL query parameter called `name`
- Uses `request.args.get()` to extract the `name` from the URL
- Returns a personalized greeting: `<h1>Hello, {name}!</h1>`
- If no name is provided, it defaults to "Guest"

**Example URLs:**
Now visit the greet route in your browser. Try the following URL querystrings in the browser tab you opened earlier:
- `/greet?name=Alice` → `Hello, Alice!`
- `/greet?name=Bob` → `Hello, Bob!`
- `/greet` → `Hello, Guest!`

**Learning point:**
- This demonstrates **dynamic content based on URL parameters**
- The server receives data from the URL and uses it to customize the response
- The same route produces different output depending on input

---

#### Route 3: `@app.route("/status")`
**Function:** `status()`

**What it does:**
- Creates a Python variable with system status information
- Uses `render_template()` to load an HTML template file (`templates/status.html`)
- Passes the Python variable to the template as a parameter
- Jinja2 templating inserts the variable into the HTML before sending it to the browser

**How it works:**
1. Python code creates `system_status = "All systems operational"`
2. The template file uses `{{ status }}` as a placeholder
3. Flask replaces `{{ status }}` with the actual value before returning the page

**Learning point:**
- Now visit `/status` in your browser to see the response
- This demonstrates **server-side templating**
- The server generates HTML dynamically by inserting Python variables into templates
- This is more powerful than string formatting because templates can have complex HTML structure with multiple dynamic values

---

#### Route 4: `@app.route("/name.html")`
**Function:** `name()`

**What it does:**
- Uses `send_from_directory()` to serve a static HTML file from the `static/` directory
- Does NOT perform any server-side processing
- Simply returns the `static/name.html` file as-is

**Learning point:**
- In your browser, visit `/name.html`
- This demonstrates **serving static files**
- Static files are not processed by the server; they're just sent to the browser unchanged
- This is useful for serving form pages, images, CSS, JavaScript, etc.

---

#### Route 5: `@app.route("/submit", methods=["POST"])`
**Function:** `submit()`

**What it does:**
- Accepts HTTP POST requests (form submissions)
- Extracts form data using `request.form["username"]`
- Renders a template with the submitted data
- Returns a page showing the user's name and explaining the client-server interaction

**How it works:**
1. User fills out the form on `/name.html` and clicks "Submit"
2. The form sends a POST request to `/submit` with the username data
3. Python code extracts the username from the POST request
4. The `templates/result.html` template is rendered with the username
5. Jinja2 inserts the username into the HTML using `{{ name }}`
6. The customized HTML page is returned to the browser

**Learning point:**
- This demonstrates **form handling and POST requests**
- The server receives data from the user (not via URL, but via form submission)
- The server processes that data and uses it to create a personalized response
- This shows the complete client-server interaction cycle

---

## Key Concepts Summary

| Route | Method | Input | Processing | Output |
|-------|--------|-------|-----------|--------|
| `/` | GET | None | Static response | Hardcoded HTML |
| `/greet` | GET | URL parameter | Extract & format | Dynamic text |
| `/status` | GET | Python variable | Template rendering | HTML with variable |
| `/name.html` | GET | None | File serving | Static HTML file |
| `/submit` | POST | Form data | Extract & template | HTML with form data |

---

## Student Activity Flow

**Hands on exercises**
1. Modify the `/` route to display a different message
2. Add a new variable to the status template
3. Create a brand new route at `/practice`. Follow the instructions in `app.py`


---
