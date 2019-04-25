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
        assert result[i][0] is i + 1


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
    assert result[0][0] is 1


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
    assert result[0][0] is 1

    alarm = repo.find_by_id(result[0][0])
    assert alarm[0] is result[0][0]


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
        assert result[i][0] is i + 1
        repo.update(Alarm(
                id=i + 1,
                name=result[i][1],
                hour=result[i][2] + 1,
                minute=result[i][3],
                last_activated=result[i][3]
            ))

    result = repo.find_all()
    assert len(result) is 10

    for i in range(len(result)):
        assert result[i][0] is i + 1
        assert result[i][2] is i+2