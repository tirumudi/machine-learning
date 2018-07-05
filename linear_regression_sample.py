# -*- coding: utf-8 -*-
import csv
from sklearn import linear_model
import numpy as np
from matplotlib import pyplot as plt

dates=[]
prices=[]

def get_data(filename):
    with open(filename,'r') as csvfile:
        csvfilereader = csv.reader(csvfile)
        next(csvfilereader)
        for row in csvfilereader:
            dates.append(int(row[0]))
            prices.append(float(row[1]))
    return

def predict_price(dates,prices,x):
    linear_mod = linear_model.LinearRegression()
    print(dates)
    dates = np.reshape(dates,(len(dates),1))
    prices = np.reshape(prices,(len(prices),1))
    print(dates)
    linear_mod.fit(dates,prices)
    y = linear_mod.predict(x)
    return y,linear_mod.coef_[0][0],linear_mod.intercept_

def show_plot(dates,prices):
    linear_mod = linear_model.LinearRegression()
    dates = np.reshape(dates,(len(dates),1))
    prices = np.reshape(prices,(len(prices),1))
    linear_mod.fit(dates,prices)
    plt.scatter(dates,prices,color="yellow")
    plt.plot(dates,linear_mod.predict(dates),color="blue",linewidth=3)
    plt.show()
    return

def printSomeusefulData():
    predicted_price, coefficient, constant = predict_price(dates,prices,29)
    print('The stock open price for 29th Feb is: $',str(predicted_price))
    print('The regression coefficient is' ,str(coefficient),', and the constant is ', str(constant))
    print('The relationship equation between dates and prices is: price = ',str(coefficient),'* date + ',str(constant))

get_data('data\google_stock_data.csv')
show_plot(dates,prices)
predicted_price,coef,intercept = predict_price(dates,prices,29)
print('predicted price for 29 : ' + str(predicted_price))
print('coefficient : '+str(coef))
print('intercept : ',str(intercept))
printSomeusefulData()

    
    
    
    

