#!/usr/bin/python3
import datetime, uuid


class BaseModel:
    def __init__(self):
        self.created_at = str(datetime.datetime.now())
        self.id = str(uuid.uuid4())

    def save(self):
        self.updated_at = str(datetime.datetime.now())

    def __str__(self):
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        dupe = self.__dict__.copy()
        dupe["__class__"] = type(self).__name__
        return dupe