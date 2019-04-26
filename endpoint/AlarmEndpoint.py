from flask import jsonify

from db.entity.Alarm import Alarm
from db.repository.AlarmJSONConverter import AlarmJSONConverter
from db.repository.AlarmRepository import AlarmRepository


class AlarmEndpoint:
    def delete_alarm(self, alarm_as_dict):
        if "id" not in alarm_as_dict:
            return "Invalid Update Request: Entitiy id is missing"

        entity = self.convert_dict_to_alarm(alarm_as_dict)
        AlarmRepository().delete(entity)

        return "200"

    def update_alarm(self, alarm_as_dict):
        if "id" not in alarm_as_dict:
            return "Invalid Update Request: Entitiy id is missing"

        entity = self.convert_dict_to_alarm(alarm_as_dict)
        entity = AlarmRepository().update(entity)

        if entity is not None:
            return jsonify(AlarmJSONConverter().alarm_to_json(entity))
        else:
            return "400: Alarm not found"

    def get_alarms(self):
        alarms = AlarmRepository().find_all()
        return jsonify(
            AlarmJSONConverter().alarm_list_to_json(alarms)
        )

    def post_alarm(self, alarm_as_dict):
        alarm = self.convert_dict_to_alarm(alarm_as_dict)
        alarm = AlarmRepository().insert(alarm)
        return jsonify(AlarmJSONConverter().alarm_to_json(alarm))

    def convert_dict_to_alarm(self, alarm_as_dict):
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
