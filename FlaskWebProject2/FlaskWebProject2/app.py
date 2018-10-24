"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route("/")
def hello():
	message = "Hello world"
	return render_template("form.html", message = message)

@app.route("/result", methods = ["POST"])
def result():
    message = "This is paiza"
    article = request.form["article"]
    name = request.form["name"]
    return render_template("form.html", message = message, article = article, name = name)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
