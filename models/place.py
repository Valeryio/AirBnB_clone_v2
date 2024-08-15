#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import *
from sqlalchemy.orm import relationship
# from models.amenity import Amenity


HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    from models.base_model import BaseModel, Base

    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = "places"

        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        amenity_id = Column(String(60), nullable=False)

        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)

        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)

        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        cities = relationship("City", back_populates="places")
        users = relationship("User", back_populates="places")
        reviews = relationship("Review", back_populates="places")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")

    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
               primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
               primary_key=True, nullable=False)
    )

else:
    from models.base_model import BaseModel

    class Place(BaseModel):
        """ A place to stay """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
