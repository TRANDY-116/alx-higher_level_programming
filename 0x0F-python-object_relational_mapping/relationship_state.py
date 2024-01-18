#!/usr/bin/python3

"""
Script that contains the class defination of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City

# Base = declarative_base()


class State(Base):
    """Defining the city class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City',
            backref='state',
            cascade='all, delete'
            )
