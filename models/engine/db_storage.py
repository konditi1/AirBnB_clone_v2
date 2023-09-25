#!/usr/bin/python3
"""
This module defines DBStorage class
"""
import os
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """
    Database storage engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor for DBStorage class
        """
        database = os.getenv("HBNB_MYSQL_DB") 
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD") 
        host = os.getenv("HBNB_MYSQL_HOST")
        connection_string = "mysql+mysqldb://{}:{}@{}:3306/{}"\
                .format(user, password, host, database)
        DBStorage.__engine = create_engine(connection_string, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on current database session
        """
        obj_list = [User, State, City, Amenity, Place, Review]
        obj_dict = {}

        if cls:
            result = DBStorage.__session.query(cls)
            for row in result:
                key = "{}.{}".format(cls.__name__, row.id)
                obj_dict[key] = row
        else:
            for obj in obj_list:
                result = DBStorage.__session.query(obj)

                for row in result:
                    key = "{}.{}".format(type(row).__name__, row.id)
                    obj_dict[key] = row

        return obj_dict

    def new(self, obj):
        """
        Add the object to the current database session 
        """
        DBStorage.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database sessio
        """
        if obj:
            DBStorage.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database
        """
        Base.metadata.create_all(DBStorage.__engine)
        Session = sessionmaker(bind=DBStorage.__engine, expire_on_commit=False)
        DBStorage.__session = Session()
