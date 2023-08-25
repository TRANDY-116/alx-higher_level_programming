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

    if len(argv) < 4:
        print("Usuage: script.py <username> <passwd> <db_name>")
        exit(1)

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

    states = session.query(State).order_by(State.id).first()
    if state is None:
        print('Nothing')
    else:
        print("{}: {}".format(state.id, state.name))

    states.close()
