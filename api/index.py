from flask import Flask
app = Flask(__name__)

@app.route("/api/client/g6K4Xte")
def test():
    return "make the chatgpt stuff!"
