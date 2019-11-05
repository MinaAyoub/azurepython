from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Worlds, yeeeee!"

for i in 10:
    print (i)

