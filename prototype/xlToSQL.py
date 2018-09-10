# This script is to force the Excel data into table.
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tableDefine import *

import pandas as pd

# Using pandas to convert the xlsx file into dataframe
xlFile = 'RGB.xlsx'
dataFrame = pd.read_excel(xlFile, header=None)

# Change the dataframe value into list
property_id = dataFrame[0].tolist()
price = dataFrame[1].tolist()
pricePerSqFt = dataFrame[2].tolist()
tenure = dataFrame[3].tolist()
location = dataFrame[4].tolist()
size = dataFrame[5].tolist()
type = dataFrame[6].tolist()
amenities = dataFrame[7].tolist()

# Query to the database
engine = create_engine('sqlite:///property.db', echo = True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Pump the data into the class
for i in range(len(property_id)):
	property = Property(property_id[i], price[i], pricePerSqFt[i], tenure[i], location[i], size[i], type[i], amenities[i])
	session.add(property)

# commit the record the database
session.commit()
 
