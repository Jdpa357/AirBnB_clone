#!/usr/bin/python3
"""
This module contains a base model
that defines all common attributes
for other classes
"""


from datetime import datetime
from uuid import uudi4
import models


class BaseModel:
    """Template class for other classes to inherit"""

    def __init__(self, *args, **kwargs):
        """Initialization of class"""
        if kwargs:
            self.__dict__.update(kwargs)
            if "created at" in self.__dict__:
                self.created_at = datetime.strptime(self.created_at,
                                                    "%Y-%m-%dT%H:%M:%S.%f")

        if "updated_at" in self.__dict__:
                self.updated_at = datetime.strptime(self.updated_at,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
            if "__class__" in self.__dict__:
                del self.__dict__["__class__"]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the current instance """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the object."""
        json_dict = {}
        for key, value in self.__dict__.items():
            json_dict[key] = value
        json_dict['__class__'] = self.__class__.__name__
        json_dict['created_at'] = self.created_at.isoformat()
        json_dict['updated_at'] = self.updated_at.isoformat()
        return json_dict
