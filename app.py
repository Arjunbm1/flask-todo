from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<h1>Hello, World!</h2>"

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "main":
    app.run(debug=True, host="0.0.0.0")