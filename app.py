from logging import debug
from flask import Flask,render_template,request
import utils
import pickle
from utils import preprocessdata
import numpy as np 
import joblib
def preprocessdata(Gender, Married, Education, Self_Employed, ApplicantIncome,CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,Property_Area):
    test_data = [[Gender, Married, Education, Self_Employed, ApplicantIncome,
       CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
       Property_Area] ]  
    trained_model = joblib.load("model.pkl") 
    prediction = trained_model.predict(test_data) 
    return prediction 
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/', methods=['GET', 'POST'])
def predict():  
    if request.method == 'POST': 
        Gender = request.form.get('Gender')
        gender_numeric = 0 if Gender == 'male' else 1
        Married = request.form.get('Married')
        Married_numeric = 0 if Married == 'yes' else 1
        Education = request.form.get('Education1')
        Education_numeric = 0 if Education == 'yes' else 1
        Self_Employed = request.form.get('Self_Employed')
        Self_Employed_numeric = 0 if Self_Employed == 'yes' else 1  
        ApplicantIncome = request.form.get('ApplicantIncome')
        CoapplicantIncome = request.form.get('CoapplicantIncome')
        LoanAmount = request.form.get('LoanAmount')
        Loan_Amount_Term = request.form.get('Loan_Amount_Term') 
        Credit_History = request.form.get('Credit_History')
        Property_Area =request.form.get('Property_Area')  
        prediction="hello"
        print(gender_numeric)
        prediction = preprocessdata(gender_numeric, Married_numeric, Education_numeric, Self_Employed_numeric, ApplicantIncome,CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,Property_Area)
        if(prediction==1):
            prediction="yes"
        else:
            prediction="no"
        return render_template('predict.html', prediction=prediction) 
if __name__=='__main__':
    app.run(debug=True)
