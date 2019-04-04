from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/', methods=["BREW", "POST"])
def brew_coffee():
    return jsonify(
        message="Brewing coffee"
    )


if __name__ == '__main__':
    app.run()
