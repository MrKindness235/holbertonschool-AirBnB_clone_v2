#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(str(60), ForeignKey('states.id'), nullable=False)
    name = Column(str(128), nullable=False)
