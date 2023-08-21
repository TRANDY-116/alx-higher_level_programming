#!/usr/bin/python3
"""
python file that contains the class
definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import delcarative_base
from model_state import Base, State

Base = declarative_base()


class State(Base):
    """
    Defining the state class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    engine = create_engine(
            'mysql://username:password@localhost:3306/hbtn_0e_6_usa')

    # Cretae the tables
    Base.metadata.create_all(engine)
