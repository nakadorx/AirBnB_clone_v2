#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    __tablename__ = "states"

    @property
    def cities(self):
        cities_list = []
        for cts in models.storage.all(City).values():
            if cities.state_id == self.id:
                cities_list.append(cts)
        return cities_list