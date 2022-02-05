"""
Name: Nia Covington
loops.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

I certify that this assignment is entirely my own work.
"""


def average():
    total_grades= eval(input("How many grades will you enter?"))
    average_acc= 0
    # demonstrates the accumulator used for the average formula later on
    for i in range(total_grades):
        print("Enter grade:")
        numerical_grade= eval(input(""))
        average_acc= average_acc + numerical_grade
        average_grade=average_acc/total_grades
    print("The average is:", average_grade)

def tip_jar():
    total_acc= 0
    # accumulator for finding the total number of tips
    for i in range(5):
        print("How much would you like to donate?")
        donation_money= eval(input(""))
        total_acc= total_acc +donation_money
    print("Total tips: $", total_acc)

def newton():
    x =int(input("What number do you want to square root?"))
    # represents x in the equation
    improv= int(input("How many times should we improve the approximation?"))

    approx=x

    for i in range(improv):
        approx=0.5*(approx+(x/approx))
    print("The square root is approximately",approx)

def sequence():
    terms_sequence=int(input("How many terms would you like?"))
    c=1
    result=[]
    while (c<=terms_sequence):
        if(c==1):
            s=1
        elif(c%2 ==1):
            s=s+2
        result.append(s)
        c=c+1
    print(*result)

def pi():
    n=int(input("How many terms in the series?"))
    pi_acc=2
    for i in range (1,n):
        left= (2 * i)/(2 * i - 1)
        right= (2 * i)/(2 *i +1)
        pi_acc= pi_acc * left * right
    print(pi_acc)
pi()

if __name__ == '__main__':
    pass
