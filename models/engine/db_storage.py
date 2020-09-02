#!/usr/bin/python3
""" this module contains the database storage engine for AirBnB project """
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ dbstorage engine """
    __engine = None
    __session = None
    all_classes = ["State", "City", "User", "Place", "Review"]

    def __init__(self):
        """ init """
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(
                        getenv('HBNB_MYSQL_USER'),
                        getenv('HBNB_MYSQL_PWD'),
                        getenv('HBNB_MYSQL_HOST'),
                        getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ querry """
        dir = {}
        if cls is None:
            for clas in self.all_classes:
                clas = eval(clas)
                for instance in self.__session.query(clas).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    dir[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__ + '.' + instance.id
                dir[key] = instance
        return dir

    def new(self, obj):
        """ add """
        self.__session.add(obj)

    def save(self):
        """ cmt """
        self.__session.commit()

    def delete(self, obj=None):
        """ del """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create """
        Base.metadata.create_all(self.__engine)
        sin = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sin)
        self.__session = Session()

    def close(self):
        """ clsoe """
        self.__session.close()
