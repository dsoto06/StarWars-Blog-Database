import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250))
    user_email = Column(String(250))
    user_password = Column(String(250))
   
class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('characters.id'))
    character_id = Column(Integer, ForeignKey('users.id'))
    users_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    users = relationship(Users)
    characters = relationship(Characters)
  


    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')