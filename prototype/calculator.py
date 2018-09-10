# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 13:53:35 2018

@author: Asus
"""


def max_LTV(no_of_loans,desired_tenure,property_type):
    if property_type == 'pri':
        cap = 30
    else:
        cap = 25
    if no_of_loans == 0:
        if desired_tenure < cap:
            return (0.75,0.05)  #(max %, min cash %)
        else:
            return (0.55,0.1)
    elif no_of_loans == 1:
        if desired_tenure < cap:
            return (0.45,0.25)
        else:
            return (0.25,0.25)
    else:
        if desired_tenure < cap:
            return (0.35,0.25)
        else:
            return (0.15,0.25)

def ABSD(status,no_of_properties):
    if status == 'F':
        return 1.2
    elif status == 'PR':
        if no_of_properties == 0:
            return 1.05
        else:
            return 1.15
    else:
        if no_of_properties == 0:
            return 1
        elif no_of_properties == 1:
            return 1.12
        else:
            return 1.15

def BSD(price):
    if price <= 180000:
        return price * 1.01
    elif price <= 360000:
        return 180000 * 1.01 + (price - 180000) * 1.02
    elif price <= 1000000:
        return 180000 * 1.01 + 180000 * 1.02 + (price - 360000) * 1.03
    else:
        return 180000 * 1.01 + 180000 * 1.02 + 640000 * 1.03 + (price - 1000000) * 1.04

def max_CPF(age,lease,price,home_type):
    if home_type == "pri":
        if lease > 60:
            return price
        elif lease < 30 or (lease >= 30 and lease <= 60 and age + lease < 80):
            return 0
        else:
            return (lease + (55 - age))/lease * price
    else:
        if lease < 30 or (lease >= 30 and lease <= 60 and age + lease < 80):
            return 0
        elif lease > 60:
            return price

def tdsr_msr(income,debt,home_type):
    if home_type == "pri":
        return income * 0.6 - debt
    else:
        if income * 0.6 - debt > income * 0.3:
            return income * 0.3
        else:
            return income * 0.6 - debt

def max_price(max_ltv,cpf,cash):
    return ((cpf + cash)/(max_ltv[0] * 100) * 100)