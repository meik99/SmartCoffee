# Replace libraries by fake ones
import sys
import fake_rpi

from flask import Flask
from flask import jsonify

from db.entity.Alarm import Alarm
from db.repository.AlarmJSONConverter import AlarmJSONConverter
from db.repository.AlarmRepository import AlarmRepository

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


@app.route('/alarm', methods=["GET"])
def get_alarms():
    alarms = AlarmRepository().find_all()
    return jsonify(
        AlarmJSONConverter().alarm_list_to_json(alarms)
    )


if __name__ == '__main__':
    sys.modules['RPi'] = fake_rpi.RPi  # Fake RPi (GPIO)
    sys.modules['smbus'] = fake_rpi.smbus  # Fake smbus (I2C)

    app.run(host='0.0.0.0')
