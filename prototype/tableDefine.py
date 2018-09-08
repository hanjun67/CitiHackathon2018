# This script is to define the table for SQL

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# Change the .db to the name that you wanted if needed.
engine = create_engine('sqlite:///property.db', echo=True)
Base = declarative_base()

########################################################################
class Property(Base):
	""""""
	__tablename__ = "property"

	property_id = Column(Integer, primary_key=True)
	price = Column(Integer)
	pricePerSqFt = Column(Float)
	tenure = Column(Integer)
	location = Column(String)
	size = Column(Integer)
	type = Column(String)
	amenities = Column(String)
	
	
	#----------------------------------------------------------------------
	# This is used to query for creating the entries in the table
	def __init__(self, property_id, price, pricePerSqFt, tenure, location, size, type, amenities):
		""""""
		self.property_id = property_id
		self.price = price
		self.pricePerSqFt = pricePerSqFt
		self.tenure = tenure
		self.location = location
		self.size = size
		self.type = type
		self.amenities = amenities

		
# create tables
Base.metadata.create_all(engine)