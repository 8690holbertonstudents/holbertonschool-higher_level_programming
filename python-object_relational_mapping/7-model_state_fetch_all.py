#!/usr/bin/python3
"""
Python module that lists all State objects from the database hbtn_0e_6_usa
Usinng module SQLAlchemy
Import State and Base from the model_state module
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection_string = (
        f"mysql+mysqlconnector://{username}:{password}@localhost:3306/{database}")
    engine = create_engine(connection_string, echo=False)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        query = session.query(State).order_by(State.id.asc()).all()
        for state in query:
            print(f"{state.id}: {state.name}")
