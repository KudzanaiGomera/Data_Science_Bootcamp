'''
Created on 4 Oct 2018

@author: Kudzanai Gomera
Build a function maximum_home_loan_with-age(PMT,i,start_age) that calculates the maximum home that your customer can afford if they,
- can afford to pay an amount ,PMT at the END of every YEAR on their birthday(starting from their next birthday)
- at an interest rate of i% per year,compounded annually
-they just turned n years old and they
-pay off the loan until they turn 65 years old i.e their last payment is on their 65th birthday
-Assume that start_age is an int value and start_age<65
-use the present value of annuity formula AKA discounted cash flow valuation
Test with
    maximum_home_loan_with_age(15000*12,0.1045,35)==1635153.79

'''
def maximum_home_loan_with_age(PMT, i, start_age):
    
    """
    
    start_age is less than 65(start_age<65)
    so time period=65-start_age
    PMT is the amount paid every birthday
    i is the interest rate per annum
    n is the start age
    """
    

    total_present_value=PMT*((1-(1/(1+i)**(65-start_age)))/i)

    PV = round(total_present_value, 2)
    return PV

