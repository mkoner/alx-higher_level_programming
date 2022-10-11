#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter a from the database
Using module SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    Base.metadata.create_all(engine)
    states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()
    for deleted in states_to_delete:
        session.delete(deleted)
    # commit and close session
    session.commit()
    session.close()
