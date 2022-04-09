"""
Nia Covington
hw10.py
Create multiple programs using knowledge drawn in throughout the class.
I certify this is my own work.
"""

def fibonacci(n):
    if n < 1:
        return None
    elif n==1 or n==2:
        sum=1
        return sum
    elif n>2:
        equation= fibonacci(n-1) + fibonacci(n-2)
        print(equation)
def double_investment(principle,rate):
    a = principle * (1 + rate)
    year=1
    while a <principle *2:
        a= a * (1+rate)
        year +=1
    else:
        return year
def syracuse(n):
    sequence= []
    sequence.append(n)
    while n != 1:
        if n % 2==0:
            n /= 2
        else:
            n= (3 * n) + 1
        sequence.append(int(n))
    return sequence

def goldbach(n):
    primes=[]
    x=3
    while x<100:
        y=1
        while y <x:
            if x % y==0:
                y=1
                continue

        else=
            primes.append(x)
        x += 2
    return primes

    output=[]
    if n % 2 ==1:
        return None
    elif n <=2:
        return "Not greater than 2"
