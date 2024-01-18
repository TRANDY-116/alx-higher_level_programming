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

    cities_by_state = session.query(City).order_by(City.id)

    # Display results
    for city in cities_by_state:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # close the session
    session.close()
