from flask import Flask
app = Flask(__name__)

@app.route("/api/v1/chat/completions")
def test():
    return "make the chatgpt stuff!"

@app.route("/api/v1/processing")
def test():
    return "working api!"
