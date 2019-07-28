# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:08:38 2019

@author: JFK3
"""

## Bisection Search. Takes balance and annual interest Rate and returns a fixed payment
def bisection(balance,annualinterestRate):
    monthlyIR = annualinterestRate/12.0
    new_balance = balance
    monthly_lower = balance/12
    monthly_upper = (balance * (1 + monthlyIR)**12)/12.0
    epsilon = 0.01
    print(monthly_lower,monthly_upper)

    
    while abs(new_balance) >=  epsilon:
        new_balance = balance
        print(monthly_lower,monthly_upper)
        payment = (monthly_upper + monthly_lower)/2
        for i in range(12):
            new_balance -= payment
            new_balance *= monthlyIR
        if new_balance > 0:
            monthly_lower = payment
        else: 
            monthly_upper = payment
        
        
            
    return round(payment,2)
            
        
    
    