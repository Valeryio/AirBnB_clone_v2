#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base, BaseModel
from sqlalchemy import *
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False, default="NULL")
    first_name = Column(String(128), nullable=False, default="NULL")
    last_name = Column(String(128), nullable=False, default="NULL")

    places = relationship("Place", back_populates="users")
    reviews = relationship("Review", back_populates="users")
    # cities = relationship("City", back_populates="cities")
