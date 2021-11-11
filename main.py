from flask import Flask, request, Response 

app = Flask(__name__)

movie_db = {
    "1" : { "name" : "Stargate", "Release Date" : "1994"},
    "2" : { "name" : "Sunshine", "Release_Date" : "2007"},
    "3" : { "name" : "The Holiday", "Release Date" : "2006" }
}

@app.route("/")
def hello():
    return "Hello World"

@app.route("/hello")
def world():
    return "<h1> Hello you !!! </h1>"

@app.route("/movies")
def Movies():
    return movie_db

if __name__ == "__main__":
    app.run(host='127.0.0.1')