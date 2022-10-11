#!/usr/bin/python3
"""adds the State object “California”
with the City “San Francisco”
to the database hbtn_0e_100_usa"""

if __name__ == "__main__":

    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    city_to_add = City(name='San Francisco')
    state_to_add = State(name='California')
    state_to_add.cities.append(city_to_add)
    session.add_all([state_to_add, city_to_add])
    session.commit()
    session.close()
