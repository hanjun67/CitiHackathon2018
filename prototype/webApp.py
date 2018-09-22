from flask import Flask, g
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tableDefine import *
from calculator import * 
import sqlite3 as sql
engine = create_engine('sqlite:///ppt.db', echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()
app = Flask(__name__)


# For tracking the usage
from flask_sqlalchemy import SQLAlchemy
from flask_track_usage import TrackUsage
from flask_track_usage.storage.sql import SQLStorage

database = '/ppt.db'
def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(database)
	return db


# PostgreSQL Setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ppt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
sql_db = SQLAlchemy(app)

# Track Usage Setup
# mstore = MongoEngineStorage()
pstore = SQLStorage(db=sql_db)
t = TrackUsage(app, [pstore])



@app.route('/')
def home():
    return render_template("homepage.html")

	
@app.route('/property_form', methods=['POST', 'GET'])
def property_form():
    
    if request.method == "POST":
		# Retrieve buyer citizenship
        buying_buying_status = request.form['buyAs']
		# Retrieve buyer number of home
        no_of_properties = int(request.form['noHome'])
		# Retrieve buyer type of home
        property_type = request.form['typeHome']
		
		
		# Retrieve the result of monthly income
        monthly_income = int(request.form['monthlyIncome'])
		# Retrieve the result of variable income
        variable_income = int(request.form['variableIncome'])
		
		
		# Retrieve the result of funds
        cpf_fund = int(request.form['cpfFund'])
		# Retrieve the result of cash
        cash = int(request.form['cash'])
			
		# Retrieve all the result of the debt
		# Retrieve the result of credit card payment per month
        credit_card = int(request.form['creditCard'])
		# Retrieve the result of car loan
        car_loan = int(request.form['carLoan'])
		# Retrieve the result of number of loan
        no_of_loan = int(request.form['noLoan'])
		# Retrieve the result of housing loan
        home_loan = int(request.form['homeLoan'])
		# Retrieve the result of other loan
        other_loan = int(request.form['otherLoan'])
		# Retrieve the result of loan tenure left over
        desired_tenure = request.form['loanTenure']
        desired_tenure = int(desired_tenure)
		
		# To calculate the gross income
        gross_income = monthly_income + variable_income * 0.7 / 12
		# To calculate the total fund available for purchase
        total_fund = cpf_fund + cash
		# To calculate teh total debt 
        debt = credit_card + car_loan + home_loan + other_loan
		

		# predefine variable for the value to calculate the price for query of database property
        int_rate = 3.5
        monthly_income = tdsr_msr(gross_income, debt, property_type)
        ltv = max_LTV(no_of_loan , desired_tenure, property_type)
        absd_value = ABSD(buying_buying_status, no_of_properties)
        max_loan = max_loan_amount(monthly_income, int_rate, desired_tenure)
		
		# To determine the max property price.
        max_property_price = max_price(cash, cpf_fund, absd_value, ltv, max_loan)
		
        session['max_property_price'] = max_property_price
		
        return render_template("property_form.html", max_property_value = max_property_price)




@app.route('/property_list', methods=['POST', 'GET'])
def list_property():
    if request.method == "POST":
        # To list down the property according to our calculator
        
        max_property_value = session.get('max_property_price')
        connect_sql = sql.connect('ppt.db')
        connect_sql.row_factory = sql.Row
		
        cur = connect_sql.cursor()
        prop_price_str = str(int(max_property_value))
        cur.execute("select * from property where price < " + prop_price_str)
		
        data_quried = cur.fetchall();

		
        return render_template("property_list.html", data_quried = data_quried )
		
@app.route('/tracking', methods=['POST', 'GET'])
def tracking():
	# for tracking
	connect_sql = sql.connect('ppt.db')
	connect_sql.row_factory = sql.Row
	
	cur = connect_sql.cursor()
	cur.execute("select * from flask_usage")
	data_quried = cur.fetchall();
	return render_template("tracking.html", data_quried = data_quried)
		

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5000)




