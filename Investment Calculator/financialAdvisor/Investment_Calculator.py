'''
Created on 4 Oct 2018

@author: Kudzanai Gomera
Write a function investment(PMT,n,i) that calculates your custormer's savings at some point in the future if 
-an amount is invested at END of every year, starting with amount of PMT at the end of this year
-at an interest rate of i% per year,compounded annually
-the investment amount doubles every SECOND YEAR(cumulatively)
test with
     investment(15000,30,0.1045)==1954935238.47
'''


def investment(PMT, n, i):
    """
    PMT is investment amount that is paid at the end of the year but the first year we dont calculate interest 
    n is the time in years of investing
    i is the interest rate
    value is for the second year where the investment amount is doubled
    """
    investment_balance = 0
    value = 0
    value <= n
    
    for j in range(n):
    # if the year is the second year then the investment is going to be doubled but if not it is going to be the same
        if value % 2 == 1:
            PMT = 2 * PMT
        investment_balance = investment_balance * (1 + i)
        investment_balance = investment_balance + PMT
        value = value + 1
        

    return round(investment_balance, 2)



