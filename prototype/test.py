# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 12:46:01 2018

@author: Asus
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tableDefine import *
from calculator import * 
engine = create_engine('sqlite:///ppt.db', echo = True)
Session = sessionmaker(bind=engine)
session = Session()
q = session.query(Property).filter(Property.price < max_price(max_LTV(1,29,'pri'),120000,50000)).all()
print(q[1].tenure)