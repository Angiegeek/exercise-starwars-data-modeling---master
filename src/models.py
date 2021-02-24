import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)
class Details_of_Planets(Base):
    __tablename__ = 'details_of_planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    diameter = Column(Integer)
    roation_period = Column(Integer)
    orbital_period =  Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(Integer)
    created = Column(Date)
    edited = Column(Date)
    name = Column(String)
    url = Column(String)
    description = Column(String)
    planets_id = Column(Integer)
    photo= Column(String)
    planets_id = Column(Integer, ForeignKey ('planets.id')) 
    planets = relationship (Planets)
    
class Details_of_People(Base):
    __tablename__ = 'details_of_people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(Date)
    gender = Column(String)
    created = Column(Date)
    edited = Column(Date)
    name = Column(String)
    homeworld = Column(String)
    url = Column(String)
    description = Column(String)
    photo = Column(String)
    people_id = Column(Integer, ForeignKey ('people.id')) 
    people = relationship (People)
    
class User_Info(Base):
    __tablename__ = 'user_info'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    profile_photo = Column(String(250))
class Favourites(Base):
    __tablename__ = 'favourites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey ('people.id')) 
    people = relationship (People)
    planets_id = Column(Integer, ForeignKey ('planets.id')) 
    planets = relationship (Planets)
    user_info_id = Column(Integer, ForeignKey ('user_info.id')) 
    user_info = relationship (User_Info)
    
   # id_Planet = Column(Integer, primary_key=True)
   # id_People = Column(Integer(250), nullable=False)
  #  user_id = Column(Integrer(250), nullable=False)
   # name= Column(String(250), nullable=False)
   # url = Column(String(250), nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')