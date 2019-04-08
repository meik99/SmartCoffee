import pytest

from SqliteConnector import SqliteConnector


def test_init_connection():
    """
    Tests if a sqlite connection can be made and whether
    the "alarm" table is present in the database.
    :return:
    """

    connector = SqliteConnector()
    assert connector.is_alarm_table_present() == True
