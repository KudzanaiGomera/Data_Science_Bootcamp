'''
Created on 4 Oct 2018

@author: Kudzanai Gomera

-Build a function retirement_age(PMT,i,FV,start_age) that calculates the whole age at which your customer can retire if they
--invest an amount PMT at the end of every YEAR( with ist payment made exactly one year from now)
--at an interest rate of i% per year compounded annually
--they require an amount of at least FV in order to be able to afford retirement
--They just turned start_age year old
test with
    retirement_age(20000,0.1,635339.63,20)==35
'''

def retirement_age(PMT, i, FV, start_age):
    """
    PMT amount paid at the end of the year
    i is the interest rate
    FV if the future value
    start age
     FV= PMT*((1+i)**(end_age-start_age)-1)/i
    FV=(PMT*i)
    """
    
    P=PMT
    age=start_age + 1
    while (P < FV):
        P+=P*i
        P+=PMT
        age+=1
    
        
    return int(age)

