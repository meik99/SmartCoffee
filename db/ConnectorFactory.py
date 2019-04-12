from db.Connector import Connector
from db.SqliteConnector import SqliteConnector


class ConnectorFactory:
    def build_connector(self) -> Connector:
        return SqliteConnector()
