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
    from sqlalchemy.sql.expression import update
    import sys

    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    connection_string = (f"mysql+mysqldb://{usr}:{pwd}@localhost:3306/{db}")
    engine = create_engine(connection_string, echo=None)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    st_update = update(State).where(State.id == 2).values(name="New Mexico")
    session.execute(st_update)
    session.commit()

    session.close()
    engine.dispose()
