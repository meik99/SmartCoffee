from db.entity.Entity import Entity
from datetime import datetime


class Alarm(Entity):
    def __init__(self, id=0, name="Alarm", hour=0, minute=0, last_activated=datetime.now()):
        self.id = id
        self.name = name
        self.hour = hour
        self.minute = minute
        self.last_activated = last_activated
