#!/usr/bin/python3
"""
Python module that lists all State objects from the database hbtn_0e_6_usa
Usinng module SQLAlchemy
Import State and Base from the model_state module
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    import sys

    connection_string = (
        f"mysql+mysqlconnector://{sys.argv[1]}:{sys.argv[2]}"
        f"@localhost:3306/{sys.argv[3]}")
    engine = create_engine(connection_string, echo=None)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()

    for row in states:
        print(f"{row.id}: {row.name}")

    session.close()
    engine.dispose()
