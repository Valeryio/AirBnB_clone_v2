#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.orm import relationship


HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"

        name = Column(String(128), nullable=False)

        cities = relationship("City", back_populates="states")
else:
    class State(BaseModel):
        """ State class """
        name = ""