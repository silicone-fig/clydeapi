from flask import Flask
app = Flask(__name__)

@app.route("/api/v1/completions")
def test():
    return "working api!"
