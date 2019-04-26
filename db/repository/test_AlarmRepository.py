import pytest

from db.ConnectorFactory import ConnectorFactory
from db.entity.Alarm import Alarm
from db.repository.AlarmRepository import AlarmRepository


@pytest.fixture(autouse=True)
def clear_db():
    ConnectorFactory().build_connector().clear_db()


def test_find_alarms():
    repo = AlarmRepository()

    for i in range(10):
        repo.insert(Alarm(
            "Alarm {}".format(i),
            hour=i + 1,
            minute=i
        ))

    result = repo.find_all()
    assert len(result) is 10

    for i in range(len(result)):
        assert result[i].id is i + 1


def test_insert_alarms():
    repo = AlarmRepository()
    alarm = Alarm(
        name="Alarm 1",
        hour=6,
        minute=0
    )
    repo.insert(alarm)
    result = repo.find_all()
    assert len(result) is 1
    assert result[0].id is 1


def test_find_by_id():
    repo = AlarmRepository()
    alarm = Alarm(
        name="Alarm 1",
        hour=6,
        minute=0
    )
    repo.insert(alarm)
    result = repo.find_all()

    assert len(result) is 1
    assert result[0].id is 1

    alarm = repo.find_by_id(result[0].id)
    assert alarm.id is result[0].id


def test_update():
    repo = AlarmRepository()

    for i in range(10):
        repo.update(Alarm(
            name="Alarm {}".format(i),
            hour=i + 1,
            minute=i
        ))

    result = repo.find_all()
    assert len(result) is 10

    for i in range(len(result)):
        assert result[i].id is i + 1
        result[i].hour = result[i].hour + 1
        repo.update(result[i])

    result = repo.find_all()
    assert len(result) is 10

    for i in range(len(result)):
        assert result[i].id is i + 1
        assert result[i].hour is i+2


def test_delete():
    repo = AlarmRepository()

    for i in range(10):
        repo.update(Alarm(
            name="Alarm {}".format(i),
            hour=i + 1,
            minute=i
        ))

    result = repo.find_all()
    assert len(result) is 10

    for i in range(len(result)):
        assert result[i].id is i + 1
        repo.delete(result[i])

    result = repo.find_all()
    assert len(result) is 0
