import threading
from datetime import datetime
from time import sleep

from flask import jsonify

from db.repository.AlarmRepository import AlarmRepository


class AlarmThread(threading.Thread):
    def __init__(self, testing=False):
        threading.Thread.__init__(self)
        self.running = True
        self.alarm_repo = AlarmRepository()

        if testing is False:
            from Tassimo import Tassimo
            self.tassimo = Tassimo()
        else:
            self.tassimo = None

    def run(self):
        while self.running is True:
            alarms = self.alarm_repo.find_all()
            now = datetime.now()

            for alarm in alarms:
                datetime_obj = datetime.strptime(alarm.last_activated, "%Y-%m-%d %H:%M:%S.%f")

                if alarm.hour == now.hour and alarm.minute == now.minute:
                    if datetime_obj.day != now.day or \
                            datetime_obj.month != now.month or \
                            datetime_obj.year != now.year or \
                            datetime_obj.hour != now.hour or \
                            datetime_obj.minute != now.minute:
                        print("Activated Alarm " + str(alarm.id) + " : " + alarm.name)
                        alarm.last_activated = now
                        self.alarm_repo.update(alarm)

                        if self.tassimo is not None:
                            self.tassimo.make_coffee()

            sleep(0.5)
