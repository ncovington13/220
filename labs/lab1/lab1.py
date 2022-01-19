"""
Nia Covington
Monthly Interest
Create a program that will allow for certain inputs and output a monthly interest charge
I certify that this is my own work.
"""

def monthly_interest():
    annual_rate= eval(input("What is the annual interest rate?"))
    # represents the percentage of the annual interest rate
    billing_cycle= eval(input("How long is the billing cycle?"))
    # indicates how many days the billing cycle is
    net_balance= eval(input("What is the net balance of account?"))
    # indicates the given balance
    payment= eval(input("What is the amount payed on the account?"))
    # gives the amount of money payed on the account
    day_payed= eval(input("What day of the cycle was the payment payed?"))
    # value is used in Step 2
    step_1=net_balance*billing_cycle
    #display result to user
    print("The amount for Step 1 is", "$" ,step_1, end="\n")
    step_2=payment*(billing_cycle-day_payed)
    #display result to user
    print("The amount for Step 2 is", "$" ,step_2, end="\n")
    step_3=step_1-step_2
    #display result to user
    print("The amount for Step 3 is", "$" ,step_3, end="\n")
    step_4=step_3/billing_cycle
    #display result to user
    print("The amount for Step 4 is", "$" ,step_4, end="\n")
    monthly_interest_charge=step_4*(annual_rate/12)/100
    #display result to user
    print("The monthly interest charge is", "$", monthly_interest_charge, end="\n")
monthly_interest()