#!/usr/bin/python3
"""
Python module that contains the class definition of a city
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Create City class that inherits from Base class

    Args:
        __tablename__: name of the table in the database
        id: The primary key of the table (auto-generated, not null)
        name: The name of the state (not null)
        state_id: The id of the state (not null, foreign key)
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
