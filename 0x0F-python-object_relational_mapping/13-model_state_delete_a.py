#!/usr/bin/python3
"""
Script that changes the name of
a state object in the database Hbtn_0e_6_usa

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

    Base.metadata.create_all(engine)

    def delete_states_by_letter(letter):
        # Query the object based on ID
        states_to_delete = session.query(State). \
                filter(State.name.like(f'%{letter}%')).all()

        if states_to_delete:
            # Delete the name
            for state in states_to_delete:
                session.delete(state)
        else:
            return
        # commit the change
        session.commit()

    # Change the name of the State where id = 2 to New Mexico
    delete_states_by_letter("a")

    session.close()
