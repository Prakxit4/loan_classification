from datetime import date
import re
from dateutil import relativedelta
from datetime import datetime
import os
from flask import Flask, flash, redirect, request, render_template, session
import pickle

import numpy as np
import mysql.connector

from algo import DecisionTreeClassifier

app = Flask(__name__)
  

with open("model.pkl", 'rb') as f:
    model = pickle.load(f)

app.secret_key = os.urandom(100)

conn = mysql.connector.connect(
    host="localhost", user="root", password="pr2kshit", database="projects")
cursor = conn.cursor()

@app.route('/')
def home():
    if 'user_id' in session:
        return render_template("index.html")

    return render_template("login.html")


@app.route('/login')
def login():
    if 'user_id' in session:
            return redirect("/")
    return render_template("login.html")


@app.route('/register')
def register():
    if 'user_id' in session:
            return redirect("/")
    return render_template("register.html")

@app.route('/change_password')
def changePassword():
    if 'user_id' in session:
            return render_template("change_password.html")
    return render_template("login.html")

@app.route("/change_password_logic",methods=["POST"])
def change_password_logic():    
    newPassword = request.form['new-password']
    currentPassword = request.form['current-password']
    reTypePassword = request.form['retype-password']

    if(newPassword=="" or currentPassword=="" or reTypePassword==""):
        flash("All the fields are required")
        return redirect("/change_password")

    user_id=session.get("user_id")
    cursor.execute(
        """SELECT * FROM users WHERE user_id='{}'""".format(user_id))
    users = cursor.fetchall()

    if(users[0][2]==currentPassword):
        if newPassword==reTypePassword:
            cursor.execute("""UPDATE users SET password='{}' where user_id={}""".format(newPassword,user_id))

            conn.commit()

            flash('Password updated successfully!', 'error')
            return redirect("/")

        else:
            flash('Both the new passwords do not match with each other!', 'error')
            return redirect("/change_password")
            
    else:
        flash('Current password is incorrect!', 'error')
        return redirect("/change_password")
        

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form['email']
    password = request.form['password']

    if(email=="" or password==""):
        flash("All the fields are required")
        return redirect("/login")

    cursor.execute(
        """SELECT * FROM users WHERE email='{}' AND password='{}'""".format(email, password))
    users = cursor.fetchall()

    if len(users) > 0:
        session['user_id'] = users[0][0]
        if(users[0][4]=="admin"):
            return redirect("/loan_page") 
        return redirect("/")
    
    else:
        flash('Incorrect email or  password!', 'error')

    return render_template('login.html')


@app.route("/validate_register", methods=["POST"])
def validate_register():
    full_name = request.form['full-name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm-password']

    if(full_name=="" or email=="" or password=="" or confirm_password==""):
        flash("All the fields are required")
        return redirect("/register")
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        flash("Invalid email format","error")
        return redirect("/register")

    cursor.execute(
        """SELECT * FROM users WHERE email='{}'""".format(email))
    
    users = cursor.fetchall()


    if len(users) > 0:
        flash("Email already exists",'error')

        return render_template("/register.html")
    

    if (password == confirm_password):
        cursor.execute("""
            INSERT INTO `projects`.`users`
            (`full_name`,
            `password`,
            `email`)
            VALUES
            ('{}',
            '{}',
            '{}');
            """.format(full_name, password, email))
        conn.commit()
        return render_template("login.html")
      
    else:
        flash('Password do not match with each other!', 'eroor')
        return render_template("login.html")
      


@app.route("/logout")
def logout():
    session.pop("user_id")
    return redirect("/")


@app.route("/loan_page")
def loanPage():
    today=date.today()
    cursor.execute(
        """SELECT * FROM loan""")
    data = cursor.fetchall()
  
    return render_template("./loan_page.html", data=data)

@app.route("/loan_status")
def loanStatusPage():
    today=date.today()
    user_id=session.get("user_id")

    cursor.execute(
        """SELECT * FROM loan where user_id={}""".format(user_id))
    data = cursor.fetchall()
  
    return render_template("./loan_status.html", data=data)



# prediction
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        employed = request.form['employed']
        Credit = request.form['credit']
        area = request.form['area']
        applicantIncome = request.form['ApplicantIncome']
        coapplicantIncome = request.form['CoapplicantIncome']
        loanAmount = request.form['LoanAmount']
        loan_Amount_Term = request.form['Loan_Amount_Term']
        Account_No=request.form['account-no']

        if(applicantIncome=="" or coapplicantIncome=="" or loan_Amount_Term=="" or Account_No=="" or Credit==""):
            flash('All the fields are required','error')
            return redirect("/predict")
        
        ApplicantIncome = float(applicantIncome)
        CoapplicantIncome = float(coapplicantIncome)
        LoanAmount = float(loanAmount)
        Loan_Amount_Term = float(loan_Amount_Term)
        credit=float(Credit)
       
        # retrieving whether the loan is already given to that account number or not
        cursor.execute(
        """SELECT * FROM loan WHERE account_no='{}'""".format(Account_No))
        loan_data = cursor.fetchall()

        if len(loan_data) > 0:
            flash('You have already taken loan...Please complete your due to apply again!', 'error')
            return redirect("/predict")
        
          
        # gender
        if (gender == "Male"):
            male = 1
        else:
            male = 0

        # married
        if (married == "Yes"):
            married_yes = 1
        else:
            married_yes = 0

        # dependents
        if (dependents == '1'):
            dependents_1 = 1
            dependents_2 = 0
            dependents_3 = 0
        elif (dependents == '2'):
            dependents_1 = 0
            dependents_2 = 1
            dependents_3 = 0
        elif (dependents == "3+"):
            dependents_1 = 0
            dependents_2 = 0
            dependents_3 = 1
        else:
            dependents_1 = 0
            dependents_2 = 0
            dependents_3 = 0

        # education
        if (education == "Not Graduate"):
            not_graduate = 1
        else:
            not_graduate = 0

        # employed
        if (employed == "Yes"):
            employed_yes = 1
        else:
            employed_yes = 0

        # property area

        if (area == "Semiurban"):
            semiurban = 1
            urban = 0
        elif (area == "Urban"):
            semiurban = 0
            urban = 1
        else:
            semiurban = 0
            urban = 0

        ApplicantIncomelog = np.log(ApplicantIncome)
        totalincomelog = np.log(ApplicantIncome+CoapplicantIncome)
        LoanAmountlog = np.log(LoanAmount)
        Loan_Amount_Termlog = np.log(Loan_Amount_Term)

        X=[credit,  LoanAmountlog,ApplicantIncomelog, Loan_Amount_Termlog, totalincomelog,male, married_yes, dependents_1, dependents_2, dependents_3, not_graduate, employed_yes, semiurban, urban]
        
        input_array = np.array(X)
        print(input_array)
       
        prediction = model.predict([input_array])
       
        print(prediction)

        if (prediction[0] == 0.0):
            print(prediction[0])

            flash('You are not qualified to get loan!', 'error')
            return redirect("/predict")
            
        elif(prediction[0]==1.0):
            print(prediction[0])
            cursor.execute("""
           INSERT INTO `projects`.`loan`
            (
            `amount_paid`,
            `loan_amount`,
            `loan_term`,
            `date`,
            `account_no`)
            VALUES
            (0,
            '{}',
            '{}','{}','{}');
            """.format(LoanAmount,Loan_Amount_Term,date.today(),Account_No))
            conn.commit()
            flash('You are  qualified to get loan!', 'success')
            return redirect("/predict")
        

    else:
        if 'user_id' in session:
            return render_template("prediction.html")

        return redirect("/")


if __name__ == "__main__":
    
    app.run(debug=True)

