#!/usr/bin/python3
"""
base class file
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
        this class defines all common
        attributes/methods for other classes


    """

    def __init__(self, **kwargs):
        """initialize the instance of the class"""
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

    def to_dict(self):
        """return dictionary containing all keys/values of
        __dict__ of the instance.

        """
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict_repr["__class__"] = type(self).__name__
        return dict_repr

    def save(self):
        """save new informations to the class object"""
        self.updated_at = datetime.now()
        models.storage.save()
