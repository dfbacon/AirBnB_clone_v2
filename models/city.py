#!/usr/bin/python3
from models import *
from sqlalchemy import Table, Column, Integer, String, DateTime
import os


class City(BaseModel, Base):
    '''This is the 'City' class'''
    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), nullable=False, ForeignKey('states.id'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
