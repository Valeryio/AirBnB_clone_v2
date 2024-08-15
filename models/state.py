#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import *
from sqlalchemy.orm import relationship


HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    from models.base_model import BaseModel, Base

    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"

        name = Column(String(128), nullable=False)

        cities = relationship("City", back_populates="states")
else:
    from models.base_model import BaseModel
    from models.city import City

    class State(BaseModel):
        """ State class """
        name = ""
        __cities = []

        @property
        def cities(self):
            """ return the list of City objects from storage
            linked to the current State"""
            all_cities = super().save().all(City)

            for city_obj in all_cities.values():
                if city_obj.state_id == self.id:
                    self.__cities.append(city_obj)
            return self.__cities
