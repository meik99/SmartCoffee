import sqlite3 as sqlite3

DATABASE_FILE="/home/pi/tassimo.db"


class SqliteConnector:
    def get_all_tables(self):
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        result = []

        for row in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"):
            result.append(row)

        connection.close()
        return result

    def is_alarm_table_present(self):
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        alarm_tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='alarm';")

        for row in alarm_tables:
            connection.close()
            return True

        connection.close()
        return False

