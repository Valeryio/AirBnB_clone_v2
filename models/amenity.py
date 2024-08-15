#!/usr/bin/python3
""" Amenity Module for HBNB project """
import os
from sqlalchemy import *
from sqlalchemy.orm import relationship


HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    from models.base_model import BaseModel, Base

    class Amenity(BaseModel, Base):
        __tablename__ = "amenities"

        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       back_populates="amenities")
else:
    from models.base_model import BaseModel

    class Amenity(BaseModel):
        name = ""
