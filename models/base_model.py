#!/usr/bin/python3
"""
base class file - mother of all classes
"""

import uuid
from datetime import datetime
from json import JSONEncoder
from models import storage


class BaseModel:
    """
        this class defines all common
        attributes/methods for other classes


    """

    def __init__(self, **kwargs):
        """initialize the instance of the class using keyword arguments"""
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
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """save updtaed information of the class object"""
        self.updated_at = datetime.now()
        storage.save()

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
        """return the string formatted message when instance is called"""
        clName = self.__class__.__name__
        return "[{}] ({}) {}".format(clName, self.id, self.__dict__)


class BaseModelEncoder(JSONEncoder):
    """JSON Encoder for BaseModel
    """

    def default(self, o):
        """ default"""
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)
