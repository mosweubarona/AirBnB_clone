#!/usr/bin/python3
"""city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """attributes: name (str)- the name of city, state_id (str)-state id"""

    state_id = ""
    name = ""
