# Replace libraries by fake ones
import sys
import fake_rpi

from flask import Flask, request
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


@app.route('/alarm', methods=["GET", "POST", "PUT", "DELETE"])
def app_alarms():
    if request.method == "GET":
        return get_alarms()
    elif request.method == "POST":
        content = request.get_json()
        return post_alarm(content)
    elif request.method == "PUT":
        content = request.get_json()
        return update_alarm(content)
    elif request.method == "DELETE":
        content = request.get_json()
        return delete_alarm(content)
    else:
        return "Invalid Request Method"


def delete_alarm(alarm_as_dict):
    if "id" not in alarm_as_dict:
        return "Invalid Update Request: Entitiy id is missing"

    entity = convert_dict_to_alarm(alarm_as_dict)
    AlarmRepository().delete(entity)

    return "200"


def update_alarm(alarm_as_dict):
    if "id" not in alarm_as_dict:
        return "Invalid Update Request: Entitiy id is missing"

    entity = convert_dict_to_alarm(alarm_as_dict)
    entity = AlarmRepository().update(entity)

    return jsonify(AlarmJSONConverter().alarm_to_json(entity))


def get_alarms():
    alarms = AlarmRepository().find_all()
    return jsonify(
        AlarmJSONConverter().alarm_list_to_json(alarms)
    )


def post_alarm(alarm_as_dict):
    alarm = convert_dict_to_alarm(alarm_as_dict)
    alarm = AlarmRepository().insert(alarm)
    return jsonify(AlarmJSONConverter().alarm_to_json(alarm))


def convert_dict_to_alarm(alarm_as_dict):
    entity = Alarm()

    if "hour" in alarm_as_dict:
        entity.hour = alarm_as_dict["hour"]
    if "minute" in alarm_as_dict:
        entity.minute = alarm_as_dict["minute"]
    if "name" in alarm_as_dict:
        entity.name = alarm_as_dict["name"]
    if "id" in alarm_as_dict:
        entity.id = alarm_as_dict["id"]

    return entity


if __name__ == '__main__':
    sys.modules['RPi'] = fake_rpi.RPi  # Fake RPi (GPIO)
    sys.modules['smbus'] = fake_rpi.smbus  # Fake smbus (I2C)

    app.run(host='0.0.0.0')
