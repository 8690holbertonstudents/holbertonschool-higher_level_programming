#!/usr/bin/python3
"""
Python module that prints the first State object
from the database hbtn_0e_6_usa
Usinng module SQLAlchemy
Import State and Base from the model_state module
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    import sys

    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    connection_string = (f"mysql+mysqldb://{usr}:{pwd}@localhost:3306/{db}")
    engine = create_engine(connection_string, echo=None)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).first()

    if not states:
        print("No Result")
    else:
        print(f"{states.id}: {states.name}")

    session.close()
    engine.dispose()
