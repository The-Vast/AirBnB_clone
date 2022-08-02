#!/usr/bin/python3
"""
base class file
"""

import uuid
from datetime import datetime


class BaseModel:
    """
	this class defines all common
	attributes/methods for other classes


	"""

    def __init__(self, *args, **kwargs):
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
