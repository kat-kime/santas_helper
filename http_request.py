"""
Practicing HTTP requests
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "Hello, world!"


@app.route("/<int:number>")
def incrementer(number):
    return "Incremented number is " + str(number + 1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
