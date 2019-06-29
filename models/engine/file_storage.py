#!/usr/bin/python3
"""This module contains the prototype for BaseModel class"""
from models.base_model import BaseModel
import json
from os import path
from models.user import User


class FileStorage:
    """FileStorage class."""
    def __init__(self):
        """Initialize FileStorage"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        k = obj.__class__.__name__ + "." + obj.id
        self.__objects[k] = obj

    def save(self):
        """Serialises __objects to the JSON file (path: __file_path)"""
        d = {k: v.to_dict()
             for k, v in self.__objects.items()}
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

    def reset(self):
        """Reset all objects in __objects."""
        self.__objects = {}
