#!/usr/bin/python3
"""
Script that lists all the states objects from
the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':

    # Creat an engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    # Create a condfigured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()
    Base.metadata.create_all(engine)

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
