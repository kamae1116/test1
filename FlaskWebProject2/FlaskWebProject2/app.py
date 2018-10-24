"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import urllib.request as req
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
url = "http://api.aoikujira.com/kawase/xml/usd"

@app.route("/")
def hello():
	message = "Hello world"
	return render_template("form.html", message = message)
	#return "hello"

@app.route("/result", methods = ["POST"])
def result():
	res = req.urlopen(url)
	soup = BeautifulSoup(res, "html.parser")
	jpy = soup.select_one("jpy").string
	message = "This is paiza"
	article = request.form["article"]
	return render_template("form.html", message = message, article = article, jpy = jpy)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
