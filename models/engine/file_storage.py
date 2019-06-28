#!/usr/bin/python3

"""
This module contains the prototype for BaseModel class.
"""
from models.base_model import BaseModel
import json
from os import path


class FileStorage:
    """FileStorage class."""

    def __init__(self):
        """Initialize FileStorage."""
        self.file_path = "file.json"
        self.objects = {}

    @property
    def file_path(self):
        """Assigns value to file_path"""
        return self.__file_path

    @property
    def objects(self):
        """Assigns value to objects"""
        return self.__objects

    @file_path.setter
    def file_path(self, val):
        self.__file_path = val

    @objects.setter
    def objects(self, val):
        self.__objects = val

    def all(self):
        """Returns the dictionary __objects"""
        return self.objects

    def new(self, obj):
        """Sets in __objects the ob with key <obj class name>.id"""
        k = obj.__class__.__name__ + "." + obj.id
        self.__objects[k] = obj

    def save(self):
        """Serialises __objects to the JSON file (path: __file_path)"""
        d = {k: v.to_dict()
             if type(v) is not dict else v for k, v in self.__objects.items()}
        with open(self.__file_path, mode='w') as f:
            json.dump(d, f)

    def reload(self):
        """Deserialises the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        if path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                loads = json.load(f)
                for k, v in loads.items():
                    cls = v["__class__"]
                    self.new(eval(cls)(**v))
