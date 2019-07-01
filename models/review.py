#!/usr/bin/python3

"""
This is a module for the review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    place_id = ''
    user_id = ''
    text = ''
