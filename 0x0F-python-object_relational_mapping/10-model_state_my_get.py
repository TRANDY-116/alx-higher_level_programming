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
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    search = argv[4]

    # Using ilike for case-insensitive search
    states = (
            session.query(State)
            .filter(State.name.ilike(f'%{search}%'))
            .order_by(State.id).all()
            )
    if not states:
        print("Not found")
    else:
        for state in states:
            print("{}".format(state.id))
    session.close()
