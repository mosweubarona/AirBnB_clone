#!/usr/bin/python3
"""
modle for base class file for airbnb clone
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    =========
    class for BaseModel of objects
    =========
    """

    def __init__(self, *args, **kwargs):
        """initialize the instance of the class

        *args: list args
        **kwargs: dic of key-value args

        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(
                            value,
                            '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    continue

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """update the update_at with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return dictionary representaton of the instance"""
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict_repr["__class__"] = type(self).__name__
        return dict_repr

    def __str__(self):
        """return the string formated message repreentation of an instance."""
        clName = self.__class__.__name__
        return "[{}] ({}) {}".format(clName, self.id, self.__dict__)
