from datetime import datetime, timedelta
from time import sleep

import pytest
# Replace libraries by fake ones
import sys
import fake_rpi

from AlarmThread import AlarmThread
from db.ConnectorFactory import ConnectorFactory
from db.entity.Alarm import Alarm
from db.repository.AlarmRepository import AlarmRepository


@pytest.fixture(autouse=True)
def setup_alarm():
    ConnectorFactory().build_connector().clear_db()
    now = datetime.now()
    yesterday = now - timedelta(1)

    repo = AlarmRepository()
    alarm = Alarm(
        name="Alarm 1",
        hour=now.hour,
        minute=now.minute,
        last_activated=yesterday
    )
    repo.insert(alarm)


@pytest.fixture(autouse=True)
def fake_gpios():
    sys.modules['RPi'] = fake_rpi.RPi  # Fake RPi (GPIO)
    sys.modules['smbus'] = fake_rpi.smbus  # Fake smbus (I2C)


def test_exectuing_alarm():
    repo = AlarmRepository()
    alarm = repo.find_by_id(1)
    alarm.last_activated = datetime.strptime(alarm.last_activated, "%Y-%m-%d %H:%M:%S.%f")
    expected = alarm.last_activated + timedelta(1)

    alarm_thread = AlarmThread(testing=True)
    alarm_thread.start()

    sleep(1)

    alarm_thread.running = False
    alarm_thread.join(10)

    alarm = repo.find_by_id(1)
    alarm.last_activated = datetime.strptime(alarm.last_activated, "%Y-%m-%d %H:%M:%S.%f")

    assert alarm.last_activated.day is expected.day
