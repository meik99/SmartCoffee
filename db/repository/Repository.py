from db.entity import Entity


class Repository:
    def find_all(self) -> list:
        pass

    def update(self, entity) -> Entity:
        pass

    def insert(self, entity) -> Entity:
        pass

    def delete(self, entity) -> Entity:
        pass

    def find_by_id(self, entity_id) -> Entity:
        pass
