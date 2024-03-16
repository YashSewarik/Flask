from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/indi")
def hello_world_in():
    return "<p>Hello, World In</p>"

app.run(debug=True)