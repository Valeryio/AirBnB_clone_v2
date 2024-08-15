#!/usr/bin/python3
""" City Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.orm import relationship


HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")
if HBNB_TYPE_STORAGE == "db":
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """

        __tablename__ = "cities"

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

        places = relationship("Place", back_populates="cities")
        states = relationship("State", back_populates="cities")
else:
    class City(BaseModel):
        """ The city class, contains state ID and name """
        state_id = ""
        name = ""


