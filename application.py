from flask import Flask
app = Flask(__name__)

app.route("/")
def hello():
    return "Hello Worlds, yeeeekoe!"

app.route("/")
def itir():
    return "weee"
