#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """[summary]

    Args:
        BaseModel ([type]): [description]
        Base ([type]): [description]
    """
    __tablename__ = "amenities"
    name = Column(String(12), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")
