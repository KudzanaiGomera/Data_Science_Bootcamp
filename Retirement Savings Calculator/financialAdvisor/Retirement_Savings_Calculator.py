'''
Created on 4 Oct 2018

@author: Kudzanai Gomera

build a function retirement_savings(PMT,i,start_age,end_age) that calculates your savings at retirement, if  they
- invest an amount PMT at the end of every year(with the first payment in exactly one years time from now
- at i% per year interest rate compounded annually.
- they just turned start_age years old and 
- they want to retire at the age of end_age
- assume that start_age is < end_age
test with
  retirement_savings(20000,0.1,20,35)==635449.63

'''
def retirement_savings(PMT, i, start_age, end_age):
    """
     the formula for calculating savings 
    PMT is the investment amount
    end_age-start_age is the time of the payment
    i is the interest
    n=end_age - start_age
    """
    
    FV= PMT*((1+i)**(end_age-start_age)-1)/i


    FV = round(FV, 2)

    return FV


