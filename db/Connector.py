class Connector:
    def get_connection(self):
        NotImplementedError()

    def get_all_tables(self):
        NotImplementedError()

    def clear_db(self):
        NotImplementedError()