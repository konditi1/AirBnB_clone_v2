#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """ Gets the list of City instances """
        from models import storage
        state_cities = []
        cities = storage.all(City)
        
        for city in cities:
            if city.state_id == self.id:
                state_cities.append[city]

        return state_cities
