'''
Created on 4 Oct 2018

@author: Kudzanai Gomera
Write a function pay_off_period(PV,PMT,i) that calculates the minmum number of years left until a loan is fully paid off if
-the amount owned on the loan is currently equal to PV
-the loan is repaid at an amount PMT at the END of every YEAR (with the first payment exactly 1 year from now)
-at an interest rate of i% per year compounded annually

use the discounted cash flow valuation
test with
      pay_off_period(1635153,15000*12,0.1045)==30
'''

def pay_off_period(PV, PMT, i):
    """
    PMT is the repaid amount every year
    PV is the present value is equal to preowned
    i is the  interest rate per year
  
    total_present_value=PMT*((1-(1/(1+i)**n))/i)
    The loan starts at value PV.
    Every month interest is added to the loan (the PV) and a sum (PMT) is paid, reducing PV.
   
   """
    P=PV
    n=1
   
    while (P>PMT):
        P+=P*i
        P-=PMT
       
        n+=1
  
    return int(n)
    
