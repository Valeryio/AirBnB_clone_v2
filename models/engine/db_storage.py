from models.base_model import Base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.state import State
# from models.user import User

"""This is the new storage engine"""


class DBStorage:

    __engine = None
    __session = None


    def __init__(self):
        """create the engine self.__engine"""

        HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")
        HBNB_ENV = os.getenv("HBNB_ENV")

        db = f"mysql+mysqldb://{HBNB_MYSQL_DB}:{HBNB_MYSQL_USER}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_PWD}"
        engine = create_engine(db, pool_pre_ping="True")

        if HBNB_ENV == "test":
            Base.metadata.drop_all(bind=engine.connect())

        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine, expire_on_commit=False)
        self.session = scoped_session(session_factory)

    @property
    def session(self):
        """Setter of the private attribute session"""
        return self.__session

    @session.setter
    def session(self, obj):
        if obj is not None:
            self.__session = obj
        else:
            print("Empty session object!")

    def all(self, cls=None):
        """query all types of objects"""
        if cls is not None:
            result = self.session.scalars(select(cls)).all()
        else:
            result = self.session.scalars(select(City, State)).all()

        # creating a dictionary with all the object queried
        all_obj = {}
        for i in result:
            key = str(i.__class__.name) + "." + str(i.id)
            all_obj[key] = i
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
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine, expire_on_commit=False)
        self.session = scoped_session(session_factory)
