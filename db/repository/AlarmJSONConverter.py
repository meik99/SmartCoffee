class AlarmJSONConverter:
    def alarm_to_json(self, alarm):
        json = {
            "id": alarm.id,
            "name": alarm.name,
            "hour": alarm.hour,
            "minute": alarm.minute,
            "last_activated": alarm.last_activated
        }
        return json

    def alarm_list_to_json(self, list):
        json = []

        for alarm in list:
            json.append(self.alarm_to_json(alarm))

        return json
