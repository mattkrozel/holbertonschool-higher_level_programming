#!/usr/bin/python3
'''
script defines state and base class to work
with sqlalchemy
'''

from SQLAlchemy import Column, Integer, String, MetaData
from SQLAlchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    state class inherits from declar base
    attrib: base class
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
