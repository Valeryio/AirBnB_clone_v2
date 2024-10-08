#!/usr/bin/python3

import os
from sqlalchemy import *
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
import MySQLdb

HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    from models.base_model import Base
    from models.place import Place, Amenity
else:
    from models.place import Place
    from models.amenity import Amenity

"""This is the new storage engine"""


class DBStorage:

    __engine = None
    __session = None
    db_obj = {"City": City, "State": State, "User": User,
              "Place": Place, "Review": Review, "Amenity": Amenity}

    def __init__(self):
        """create the engine self.__engine"""

        HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")
        HBNB_ENV = os.getenv("HBNB_ENV")

        db = f"mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@\
{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}"

        # recreate the database if deleted by the tests
        safe_db = MySQLdb.connect(host=HBNB_MYSQL_HOST, user=HBNB_MYSQL_USER,
                                  password=HBNB_MYSQL_PWD)
        cursor = safe_db.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {HBNB_MYSQL_DB}")

        # create safely a new engine
        self.engine = create_engine(db, pool_pre_ping="True")

        if HBNB_ENV == "test":
            Base.metadata.drop_all(bind=self.engine.connect())
            # Base.metadata.drop_all(bind=self.engine.c
        """
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine, expire_on_commit=False)
        self.session = scoped_session(session_factory)
        """

    @property
    def session(self):
        """Setter of the private attribute session"""
        return self.__session

    @session.setter
    def session(self, obj):
        """setter of the private attribute engine"""
        if obj is not None:
            self.__session = obj
        else:
            print("Empty session object!")

    @property
    def engine(self):
        """getter of the private attribute engine"""
        return self.__engine

    @engine.setter
    def engine(self, obj):
        """setter of the private attribute engine"""
        if obj is not None:
            self.__engine = obj
        else:
            print("Engine object not set!")

    def all(self, cls=None):
        """query all types of objects"""
        session = self.session()
        all_obj = {}

        if cls is not None:
            result = session.query(cls).all()

            # creating a dictionary with all the object queried
            for i in result:
                key = str(i.__class__.__name__) + "." + str(i.id)
                all_obj[key] = i
        else:
            all_result = []
            for value in self.db_obj.values():
                all_result.append(session.query(value).all())

            # creating a dictionary with all the object queried
            for obj_list in all_result:
                for obj in obj_list:
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    all_obj[key] = obj
            # print("The result : ", all_result)
            # print("ALl the objects :", all_obj)
        return all_obj

    def new(self, obj):
        """add the object to the current database session"""
        self.session.add(obj)

    def save(self):
        """commit all changes of the current db session"""
        self.session.commit()

    def delete(self, obj=None):
        """delete obj from the current session if not None"""
        if obj is not None:
            self.session.delete(obj)

    def reload(self):
        """reload the database"""
        Base.metadata.create_all(self.engine)
        session_factory = sessionmaker(bind=self.engine,
                                       expire_on_commit=False)
        self.session = scoped_session(session_factory)

    def close(self):
        """close the session"""
        self.session.close_all()
