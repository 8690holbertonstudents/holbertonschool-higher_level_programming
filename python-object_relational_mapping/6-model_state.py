#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base
from sqlalchemy import create_engine

usr = sys.argv[1]
pwd = sys.argv[2]
db = sys.argv[3]

if __name__ == "__main__":
    connection_string = (f"mysql+mysqldb://{usr}:{pwd}@localhost:3306/{db}")
    engine = create_engine(connection_string, echo=None)
    Base.metadata.create_all(engine)
