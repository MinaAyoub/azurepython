from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Worlds, yeeleee!"

def itir():
    sty = "testing"
    for i in sty:
        return i
