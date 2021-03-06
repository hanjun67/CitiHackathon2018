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

def ABSD(buying_buying_status,no_of_properties):
    if buying_buying_status == 'F':
        return 0.2
    elif buying_buying_status == 'PR':
        if no_of_properties == 0:
            return 0.05
        else:
            return 0.15
    else:
        if no_of_properties == 0:
            return 0
        elif no_of_properties == 1:
            return 0.12
        else:
            return 0.15

def BSD(price):
    if price <= 180000:
        return price * 0.01
    elif price <= 360000:
        return 180000 * 0.01 + (price - 180000) * 0.02
    elif price <= 1000000:
        return 180000 * 0.01 + 180000 * 0.02 + (price - 360000) * 0.03
    else:
        return 180000 * 0.01 + 180000 * 0.02 + 640000 * 0.03 + (price - 1000000) * 0.04

def max_CPF(age,lease,price,property_type):
    if property_type == "pri":
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

def tdsr_msr(income,debt,property_type):
    if property_type == "pri":
        return income * 0.6 - debt
    else:
        if income * 0.6 - debt > income * 0.3:
            return income * 0.3
        else:
            return income * 0.6 - debt

def max_loan_amount(monthly_payment, int_rate, desired_tenure):
	# monthly_payment = tdsr_msr(income, debt, property_type)
    return round(monthly_payment * ((1 + int_rate / 100 / 12) ** (desired_tenure * 12) - 1) / (int_rate / 100 / 12 * (1 + int_rate / 100 / 12) ** (desired_tenure * 12)))

def max_price(cash, cpf_fund, absd, max_ltv, max_loan):
    def cash_cpf_optimize(cash, cpf_fund, cash_pct, cpf_pct, absd, bsd_pct, bsd_value):
        return (cash + cpf_fund + bsd_value) / (cash_pct + bsd_pct + absd + cpf_pct)
    def cash_cpf_loan_optimize(max_loan, cash, cpf_fund, cash_pct, cpf_pct, absd, bsd_pct, bsd_value): #use if cash confirm enough
        return (max_loan + cash + cpf_fund + bsd_value) / (1 + bsd_pct + absd)
    cash_pct = max_ltv[1]
    cpf_pct = 1 - max_ltv[0] - max_ltv[1]
    max_price = cash / cash_pct
    max_price_bsd = BSD(max_price)
    max_price_absd = absd * max_price
    excess_cpf = cpf_fund - max_price_bsd - max_price_absd
    if excess_cpf < 0:
        if max_price > 1000000:
            max_price = cash_cpf_optimize(cash, cpf_fund, cash_pct, cpf_pct, absd, 0.04, 15400)
        else:
            pass
        if max_price <= 1000000 and max_price > 320000:
            max_price = cash_cpf_optimize(cash, cpf_fund, cash_pct, cpf_pct, absd, 0.03, 5400)
        else:
            pass
        if max_price <= 320000 and max_price > 180000:
            max_price = cash_cpf_optimize(cash, cpf_fund, cash_pct, cpf_pct, absd, 0.02, 1800)
        else:
            pass
        if max_price <= 180000:
            max_price = cash_cpf_optimize(cash, cpf_fund, cash_pct, cpf_pct, absd, 0.01, 0)
        else:
            pass
    else:
        pass
    if max_loan + excess_cpf > 0.75 * max_price:
        return max_price
    else:
        if max_price > 1000000:
            max_price = cash_cpf_loan_optimize(max_loan, cash, cpf_fund, cash_pct, cpf_pct, absd, 0.04, 15400)
        else:
            pass
        if max_price <= 1000000 and max_price > 320000:
            max_price = cash_cpf_loan_optimize(max_loan, cash, cpf_fund, cash_pct, cpf_pct, absd, 0.03, 5400)
        else:
            pass
        if max_price <= 320000 and max_price > 180000:
            max_price = cash_cpf_loan_optimize(max_loan, cash, cpf_fund, cash_pct, cpf_pct, absd, 0.02, 1800)
        else:
            pass
        if max_price <= 180000:
            max_price = cash_cpf_loan_optimize(max_loan, cash, cpf_fund, cash_pct, cpf_pct, absd, 0.01, 0)
        else:
            pass
        return max_price