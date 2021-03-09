#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 12:41:22 2021

@author: shivadhulipala
"""


from flask import Flask,request,render_template
#import numpy as np
import pandas as pd
import joblib

# initialise flask
app = Flask(__name__,template_folder='Template')
#load model
model = joblib.load('Hotels.pkl')
# launch home page
@app.route('/',methods = ['GET'])
def home():
    print("hello")
    # load html page
    return render_template('hotels.html')

@app.route('/',methods = ['POST'])
def prediction():
    x_col=['name','city','pool', 'gym', 'spa', 'free_parking', 'bathtub', 'restuarant',
       'Airport_transfer', 'Bar', 'Kitchen', 'Connecting_rooms_available',
       'Internet_access', 'Pet_friendly', 'City Center',
       'day_in', 'month', 'year', 'day_out']
    # info from user input
    d =[[x for x in request.form.values()]]
    data = pd.DataFrame(d,columns=x_col)
    dataset=data[['name','city','pool', 'gym', 'spa', 'free_parking', 'bathtub', 'restuarant',
       'Airport_transfer', 'Bar', 'Kitchen', 'Connecting_rooms_available',
       'Internet_access', 'Pet_friendly', 'City Center',
       'day_in', 'month', 'year', 'day_out']]
    print(dataset)
    predict = model.predict(dataset)[0]
    print(predict)
    text = ("Prediction: ₹"+str(predict))
    print(text)
    return render_template('hotels.html',prediction_text = text)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
    
    











