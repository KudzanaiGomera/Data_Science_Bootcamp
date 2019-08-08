'''
Created on 4 Oct 2018

@author: Kudzanai gomera


build a function savings_calculator(PMT,n,i) that calculates your savings at retirement, if  they
- invest an amount PMT at the end of every year(with the first payment in exactly one years time from now
-n for the whole years
-i% per year interest rate compounded annually.

test with
savings_calculator(20000,15,0.1)==63449.63

'''

def savings_calculator(PMT, n, i):
    """"the formula for calculating savings
    PMT = investment amount
    n is the time of the payment
    i is the interest rate per year compounded annually
    FV= the savings or the future value
    
    we will call out the function in the ipython console after running the program
    """

    FV = PMT * ((1 + i) ** n - 1) / i

    FV = round(FV, 2)

    return FV