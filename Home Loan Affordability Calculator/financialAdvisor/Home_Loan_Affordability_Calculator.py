'''
Created on 4 Oct 2018

@author: Kudzanai Gomera

Build a function maximum_home_loan(PMT,i,n) that calculates the maximum home that your customer can afford if they,
- can afford to pay an amount ,PMT at the END of every YEAR(with ist payment made exactly one year form now)
- at an interest rate of i% per year,compounded annually
-pay off the home over a term of n years
-use the present value of annuity formula AKA discounted cash flow valuation

test with 
     maximum_home_loan(15000*12,0.1045,30)==1635153,79
'''

def maximum_home_loan(PMT, i, n):
    
    """
    
    using the discounted cash flow formula
    
    PMT is the amount paid yearly
    i is the interest rate
    n is the time
    
    """

    total_present_value=PMT*((1-(1/(1+i)**n))/i)

    PV = round(total_present_value, 2)
    return PV