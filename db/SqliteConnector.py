import sqlite3 as sqlite3

from db.Connector import Connector

DATABASE_FILE = "tassimo.db"
CREATE_TABLE_ALARM = "CREATE TABLE IF NOT EXISTS ALARM(" \
                     "ID INTEGER PRIMARY KEY, " \
                     "NAME TEXT" \
                     "HOUR INTEGER NOT NULL DEFAULT 0, " \
                     "MINUTE INTEGER NOT NULL DEFAULT 0);"
FIND_ALL_TABLES = "SELECT name FROM sqlite_master WHERE type='table';"
FIND_ALARM_TABLE = "SELECT name FROM sqlite_master WHERE type='table' AND lower(name)='alarm';"


class SqliteConnector(Connector):
    def __init__(self):
        if self.is_alarm_table_present() is False:
            self._setup_database()
            if self.is_alarm_table_present() is False:
                RuntimeError("Could not setup database")

    def _setup_database(self):
        connection = sqlite3.connect(DATABASE_FILE)
        connection.execute(CREATE_TABLE_ALARM)
        connection.commit()
        connection.close()

    def get_all_tables(self):
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        result = []

        for row in cursor.execute(FIND_ALL_TABLES):
            result.append(row)

        connection.close()
        return result

    def is_alarm_table_present(self):
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        alarm_tables = cursor.execute(FIND_ALARM_TABLE)

        for row in alarm_tables:
            connection.close()
            return True

        connection.close()
        return False

    def get_connection(self):
        return sqlite3.connect(DATABASE_FILE)

