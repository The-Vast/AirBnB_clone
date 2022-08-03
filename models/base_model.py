#!/usr/bin/python3
"""
base class file - mother of all classes
"""

import uuid
from datetime import datetime
from json import JSONEncoder


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

    def save(self):
        """updates the informations of the class object"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """return dictionary representaton (key/values) of the instance"""
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict_repr["__class__"] = type(self).__name__
        return dict_repr

    def __str__(self):
        """return the string formated message when instance is called"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


class BaseModelEncoder(JSONEncoder):
    """JSON Encoder for BaseModel
    """

    def default(self, obj):
        """ default"""
        if isinstance(obj, BaseModel):
            return obj.to_dict()
        return super().default(obj)
