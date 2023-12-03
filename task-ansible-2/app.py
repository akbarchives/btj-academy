from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, Docker!"


@app.route("/menu")
def menu():
    return "This is menu page"


@app.route("/about")
def about():
    return "This is about page"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5007)
