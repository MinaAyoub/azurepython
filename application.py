from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Worlds, yeeeee!"

for i in "LIST THIS SENTENCE":
    print (i)

