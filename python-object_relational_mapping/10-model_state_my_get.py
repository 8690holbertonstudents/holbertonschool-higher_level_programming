#!/usr/bin/python3
"""
Python module that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
Using module SQLAlchemy
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
    st_name = sys.argv[4]

    connection_string = (f"mysql+mysqldb://{usr}:{pwd}@localhost:3306/{db}")
    engine = create_engine(connection_string, echo=None)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like(st_name)).all()

    if not states:
        print("Not found")
    else:
        for rows in states:
            print(f"{rows.id}")

    session.close()
    engine.dispose()
