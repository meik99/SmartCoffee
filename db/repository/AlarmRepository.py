from db.ConnectorFactory import ConnectorFactory
from db.entity.Alarm import Alarm
from db.repository.AlarmResultConverter import AlarmResultConverter
from db.repository.Repository import Repository

FIND_ALARMS = "SELECT * FROM ALARM"
INSERT_ALARM = "INSERT INTO ALARM(NAME, HOUR, MINUTE, LAST_ACTIVATED) VALUES (?, ?, ?, ?);"
UPDATE_ALARM = "UPDATE ALARM SET NAME=?, HOUR=?, MINUTE=?, LAST_ACTIVATED=? WHERE ID = ?;"
FIND_ALARM = "SELECT * FROM ALARM WHERE ID=?;"
DELETE_ALARM = "DELETE FROM ALARM WHERE ID=?;"


class AlarmRepository(Repository):
    def find_all(self) -> list:
        result = []
        alarm_result_converter = AlarmResultConverter()
        connection = ConnectorFactory().build_connector().get_connection()
        cursor = connection.cursor()

        for row in cursor.execute(FIND_ALARMS):
            result.append(alarm_result_converter.convert_cursor_result_to_alarm(row))

        connection.close()
        return result

    def insert(self, entity) -> Alarm:
        if type(entity) is not Alarm:
            raise ValueError("'entity' must be of type 'Alarm'")

        connection = ConnectorFactory().build_connector().get_connection()
        cursor = connection.cursor()
        cursor.execute(INSERT_ALARM, (entity.name, entity.hour, entity.minute, entity.last_activated))

        entity.id = cursor.lastrowid

        connection.commit()
        connection.close()

        return entity

    def update(self, entity) -> Alarm:
        if type(entity) is not Alarm:
            raise ValueError("'entity' must be of type 'Alarm'")

        if entity.id <= 0:
            return self.insert(entity)
        else:
            connection = ConnectorFactory().build_connector().get_connection()
            cursor = connection.cursor()
            cursor.execute(UPDATE_ALARM, (entity.name, entity.hour, entity.minute, entity.last_activated, entity.id))
            connection.commit()
            connection.close()
            return self.find_by_id(entity.id)

    def find_by_id(self, entity_id) -> Alarm:
        connection = ConnectorFactory().build_connector().get_connection()
        cursor = connection.cursor()
        result = None

        for row in cursor.execute(FIND_ALARM, (entity_id,)):
            if result is not None:
                raise RuntimeError("Entities with the same id are present in the sqlite table.")
            result = row

        connection.commit()
        connection.close()

        return AlarmResultConverter().convert_cursor_result_to_alarm(result)

    def delete(self, entity):
        connection = ConnectorFactory().build_connector().get_connection()
        cursor = connection.cursor()
        cursor.execute(DELETE_ALARM, (entity.id,))

        connection.commit()
        connection.close()
