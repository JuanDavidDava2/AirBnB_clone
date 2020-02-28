#!/usr/bin/python3
"""
This module contains a base model
that defines all common attributes
for other classes
"""


from datetime import datetime
import uuid as uuid
import models


class BaseModel:
    """Template class for other classes to inherit"""

    __instances = 0

    def __init__(self, *args, **kwargs):
        """Initialization of class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = \
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)
        type(self).__instances += 1

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

    @classmethod
    def count(cls):
        return cls.__instances
