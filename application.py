from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Worlds, yeeleee!"

def itir():
    for i in "testing":
        return i
