#!/usr/bin/python3
"""
Python module that prints the first State object
from the database hbtn_0e_6_usa
Usinng module SQLAlchemy
Import State and Base from the model_state module
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    connection_string = (
        f"mysql+mysqlconnector://{usr}:{pwd}@localhost:3306/{db}")
    engine = create_engine(connection_string, echo=False)

    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)

    with Session() as session:
        query = session.query(State).order_by(State.id).first()
        print(f"{query.id}: {query.name}")
