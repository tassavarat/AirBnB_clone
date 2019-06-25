#!/usr/bin/python3

"""
This module contains the prototype for BaseModel class.
"""

from uuid import uuid4
from datetime import datetime as dt


class BaseModel():
    """BaseModel class."""

    def __init__(self):
        """Initialize BaseModel."""
        self.id = str(uuid4())
        self.created_at = dt.utcnow()
        self.updated_at = dt.utcnow()

    def __str__(self):
        """Prints : [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] () ".format(type(self), self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with
        the current datetime."""
        self.updated_at = dt.utcnow()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance."""
        d = {}
        return d
