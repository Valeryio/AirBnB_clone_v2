#!/usr/bin/python3
""" Review module for the HBNB project """
import os
from sqlalchemy import *
from sqlalchemy.orm import relationship

HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":

    from models.base_model import BaseModel, Base
    class Review(BaseModel, Base):
        """ Review classto store review information """
        __tablename__ = "reviews"

        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)

        places = relationship("Place", back_populates="reviews")
        users = relationship("User", back_populates="reviews")
else:

    from models.base_model import BaseModel
    class Review(BaseModel):
        """ Review class to store review information """
        place_id = ""
        user_id = ""
        text = ""

