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
    
    def update_state_name(state_id, new_name):
        #Query the object based on ID
        state_to_update = session.query(State).filter_by(id=state_id).first()

        if state_to_update:
            #Update the name
            state_to_update.name = new_name

            #commit the change
            session.commit()

    #Change the name of the State where id = 2 to New Mexico
    update_state_name(2, "New Mexico")

    session.close()
