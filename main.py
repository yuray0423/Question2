import os

from flask import Flask, request, render_template

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     name = os.environ.get("NAME", "World")
#     return "Hello {}!".format(name)


@app.route("/user")
def user():
    return render_template("index.html")

@app.route('/')
def hello():
    return "HELLO"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
