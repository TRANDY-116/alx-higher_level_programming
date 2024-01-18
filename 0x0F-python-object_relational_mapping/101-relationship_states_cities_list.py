#!/usr/bin/python3
"""
Script that Prints all City Objects
from the database Hbtn_0e_6_usa

"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_cities = session.query(State).order_by(State.id)

    # Display results
    for state in states_with_cities:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # close the session
    session.close()
