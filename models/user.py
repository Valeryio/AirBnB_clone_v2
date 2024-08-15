#!/usr/bin/python3
"""This module defines a class User"""
import os
from models.base_model import Base, BaseModel
from sqlalchemy import *
from sqlalchemy.orm import relationship


HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = "users"

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        # first_name = Column(String(128), default="NULL")
        first_name = Column(String(128), nullable=True)
        # last_name = Column(String(128), default="NULL")
        last_name = Column(String(128), nullable=True)

        places = relationship("Place", back_populates="users")
        reviews = relationship("Review", back_populates="users")
        # cities = relationship("City", back_populates="cities")
else:
    class User(BaseModel):
        """This class defines a user by various attributes"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
