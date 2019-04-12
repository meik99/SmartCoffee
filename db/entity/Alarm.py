from db.entity.Entity import Entity


class Alarm(Entity):
    def __init__(self, name = "Alarm", hour=0, minute=0):
        self.name = name
        self.hour = hour
        self.minute = minute
