#!/usr/bin/python3
'''
script defines state and base class to work
with sqlalchemy
'''

from SQLAlchemy import Column, Integer, String
from SQLAlchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    state class
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
