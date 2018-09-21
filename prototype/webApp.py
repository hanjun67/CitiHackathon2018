from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tableDefine import *
from calculator import * 
engine = create_engine('sqlite:///ppt.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")

	
@app.route('/property_form', methods=['POST', 'GET'])
def property_form():
    
    if request.method == "POST":
		# Retrieve buyer citizenship
        buying_status = request.form['buyAs']
		# Retrieve buyer number of home
        no_of_properties = int(request.form['noHome'])
		# Retrieve buyer type of home
        property_type = request.form['typeHome']
		
		# Retrieve the result of the income
        monthly_income = int(request.form['monthlyIncome'])
        variable_income = int(request.form['variableIncome'])
        pledged_income = int(request.form['pledgedIncome'])
        unpledged_deposit = int(request.form['unpledgedDeposit'])
		
		# Retrieve the result of the funds
        cpf_fund = int(request.form['cpfFund'])
        cash = int(request.form['cash'])
			
		# Retrieve the result of the debt
        credit_card = int(request.form['creditCard'])
        car_loan = int(request.form['carLoan'])
        no_of_loan = int(request.form['noLoan'])
        home_loan = int(request.form['homeLoan'])
        other_loan = int(request.form['otherLoan'])
        desired_tenure = request.form['loanTenure']
        desired_tenure = int(desired_tenure)
		
        gross_income = monthly_income + variable_income * 0.7 / 12
        total_fund = cpf_fund + cash
        debt = credit_card + car_loan + home_loan + other_loan
		
        # session['noHome'] = no_of_properties
        # session['loanTenure'] = desired_tenure
        # session['typeHome'] = property_type
        # session['cash'] = cash
        # session['cpf_fund'] = cpf_fund 
		
        max_property_price = max_price(max_LTV(no_of_loan , desired_tenure, property_type), cash, cpf_fund)
		
        return render_template("property_form.html", max_property_value = max_property_price, grossIncome = gross_income)	

        
        # q = session.query(Property).filter(Property.price < max_price(max_LTV(noHome,loanTenure,typeHome),cash,cpf_fund)).all()


@app.route('/property_list', methods=['POST', 'GET'])
def list_property():
    if request.method == "POST":
        # no_of_properties = session.get('noHome', None)
        # desired_tenure = session.get('loanTenure', None)
        # property_type = session.get('typeHome', None)
        # cash = session.get('cash', None)
        # cpf_fund = session.get('cpf_fund', None)
		
        return render_template("property_list.html")

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)




