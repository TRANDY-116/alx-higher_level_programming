#!/usr/bin/python3
"""
Script that Prints all City Objects
from the database Hbtn_0e_6_usa

"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Display results
    for state, city in session.query(State, City).filter(
            State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
