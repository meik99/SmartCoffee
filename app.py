from flask import Flask
from flask import jsonify

from Tassimo import Tassimo

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/', methods=["BREW", "POST"])
def brew_coffee():
    Tassimo().make_coffee()

    return jsonify(
        message="Brewing coffee"
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
