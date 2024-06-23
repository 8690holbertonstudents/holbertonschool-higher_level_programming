#!/usr/bin/python3
"""
Python module that lists all cities of a given state 
from the database hbtn_0e_14_usa
Usinng module SQLAlchemy
Import State and Base from the model_state module
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    import sys

    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    connection_string = (f"mysql+mysqldb://{usr}:{pwd}@localhost:3306/{db}")
    engine = create_engine(connection_string, echo=None)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    query = session.query(City, State).join(
        State, State.id == City.state_id, isouter=True).order_by(City.id.asc()).all()

    for city, state in query:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
    engine.dispose()
