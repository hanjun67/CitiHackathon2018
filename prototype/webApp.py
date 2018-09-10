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
	
@app.route('/requestForm_result', methods=['POST', 'GET'])
def request_form():
    if request.method == "POST":
		# Retrieve buyer citizenship
        buying_as = request.form['busAs']
        no_home = request.form['noHome']
        type_home = request.form['typeHome']
		
		# Retrieve the result of the income
        monthly_income = int(request.form['monthlyIncome'])
        variable_income = int(request.form['variableIncome'])
        pledged_income = int(request.form['pledgedIncome'])
        unpledged_deposit = int(request.form['unpledgedDeposit'])
		
		# Retrieve the result of the funds
        cpf_fund = int(request.form['cpfFund'])
        cash = int(request.form['cash'])
			
		# Retrieve the reust of the debt
        credit_card = int(request.form['creditCard'])
        car_loan = int(request.form['carLoan'])
        home_loan = int(request.form['homeLoan'])
        other_loan = int(request.form['otherLoan'])
        
        loan_tenure = int(request.form['loanTenure'])
		
        gross_income = monthly_income + variable_income * 0.7 / 12
        total_fund = cpf_fund + cash
        debt = credit_card + car_loan + home_loan + other_loan
		
        return render_template("test.html", buyAs = buying_as, loanTenure = loan_tenure,typeHome = type_home,cash = cash, cpf_fund = cpf_fund, noHome = no_home,  grossIncome = gross_income, totalFund = total_fund, debt =debt)

@app.route('/property_form', methods=['POST', 'GET'])
def property_form():
    if request.method == "POST":
        q = session.query(Property).filter(Property.price < max_price(max_LTV(noHome,loanTenure,typeHome),cash,cpf_fund)).all()
        return render_template("property_form.html")

		
@app.route('/property_list', methods=['POST', 'GET'])
def list_property():
    if request.method == "POST":
        return render_template("property_list.html")

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)




