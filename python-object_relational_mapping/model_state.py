#!/usr/bin/python3
"""
Python module that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""
create a base class called Base
ORM models will inherit from this class.
"""
Base = declarative_base()


class State(Base):
    """
    Create State class that inherits from Base class

    Args:
        __tablename__: name of the table in the database
        id: The primary key of the table (auto-generated, not null)
        name: The name of the state (not null)
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
