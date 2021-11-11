from flask import Flask, request, Response 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/hello")
def world():
    return "<h1> Hello you !!! </h1>"

if __name__ == "__main__":
    app.run(host='127.0.0.1')