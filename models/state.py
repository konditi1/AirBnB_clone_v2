#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(City, backref="state")

    @property
    def cities(self):
        """ Gets the list of City instances """
        state_cities = []
        for city in self.city:
            if city.state_id == self.id:
                state_cities.append[city]

        return state_cities
