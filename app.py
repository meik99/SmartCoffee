# Replace libraries by fake ones
import sys
import fake_rpi

from flask import Flask, request
from flask import jsonify

from AlarmThread import AlarmThread
from endpoint.AlarmEndpoint import AlarmEndpoint

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/coffee', methods=["BREW", "POST"])
def brew_coffee():
    from Tassimo import Tassimo
    Tassimo().make_coffee()

    return jsonify(
        message="Brewing coffee"
    )


@app.route('/alarm', methods=["GET", "POST", "PUT", "DELETE"])
def app_alarms():
    endpoint = AlarmEndpoint()

    if request.method == "GET":
        return endpoint.get_alarms()
    elif request.method == "POST":
        content = request.get_json()
        return endpoint.post_alarm(content)
    elif request.method == "PUT":
        content = request.get_json()
        return endpoint.update_alarm(content)
    elif request.method == "DELETE":
        content = request.get_json()
        return endpoint.delete_alarm(content)
    else:
        return "Invalid Request Method"


if __name__ == '__main__':
    sys.modules['RPi'] = fake_rpi.RPi  # Fake RPi (GPIO)
    sys.modules['smbus'] = fake_rpi.smbus  # Fake smbus (I2C)

    alarm_thread = AlarmThread(testing=True)
    alarm_thread.setDaemon(True)
    alarm_thread.start()

    app.run(host='0.0.0.0')
