from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h2>Hello, World!</h2>"

@app.route("/about")
def about():
    return "<h2>About Page.</h2>"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
