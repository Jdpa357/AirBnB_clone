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
