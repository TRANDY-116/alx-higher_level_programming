#!/usr/bin/python3
"""
Script that lists all State objects
from the database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .fromat(argv[1], argv[2], argv[3]),
            pool_pre_ping=True
            )
