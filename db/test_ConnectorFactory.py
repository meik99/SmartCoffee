from db.Connector import Connector
from db.ConnectorFactory import ConnectorFactory


def test_get_connector():
    connector_factory = ConnectorFactory()
    connector = connector_factory.build_connector()

    assert connector is not None
