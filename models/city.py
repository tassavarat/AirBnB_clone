#!/usr/bin/python3

"""
This is a module for the city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""
    state_id = ''
    name = ''
