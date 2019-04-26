from db.entity.Alarm import Alarm


class AlarmResultConverter:
    def convert_cursor_result_to_alarm(self, cursor_alarm_result) -> Alarm:
        return Alarm(
            id=cursor_alarm_result[0],
            name=cursor_alarm_result[1],
            hour=cursor_alarm_result[2],
            minute=cursor_alarm_result[3],
            last_activated=cursor_alarm_result[4]
        )
