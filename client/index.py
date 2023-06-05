from flask import Flask
app = Flask(__name__)

@app.route("/client/g6K4Xte")
def test():
    return "working api"
