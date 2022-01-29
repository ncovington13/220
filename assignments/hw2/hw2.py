"""
Name: Nia Covington
arthimetic.py

Problem: These programs takes problems or questions and apply arithmetic methods to give outputs based on the inputs.


I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound?"))
    upper_for_three = upper_bound// 3
    total_sum = 3* upper_for_three*(1+ upper_for_three)/2
    # formula used to solve for the sum
    print("The sum of three is", total_sum)


def multiplication_table():
    for x in range (1, 11):
        for y in range (1,11):
            print(x*y, end=" ")
        print()

def triangle_area():
    side_a = float(input("What is the length of side A?"))
    side_b = float(input("What is the length of side B?"))
    side_c = float(input("What is the length of side C?"))
    s = (side_a + side_b + side_c) / 2
    # represents equation necessary for next part of the equation
    area_1 = s - side_a
    area_2 = s - side_b
    area_3 = s - side_c
    # represents different part of the area equation given
    total_area = math.sqrt(s * area_1 * area_2 * area_3)
    print("The area is", total_area)



def sum_squares():
    lower_range = eval(input("Enter the lower range:"))
    upper_range = eval(input("Enter the upper range:"))
    total = 0
    for i in range(lower_range,upper_range+1):
        total = i * i
    print(total)

def power():
    base = int(input("Enter base:"))
    exponent = int(input("Enter exponent:"))
    ans=1
    # accumulator for the answer to the power
    for i in range(exponent):
        ans=ans*base
        # formula that gives the answer to the power
    print(base,"^",exponent,"=", ans)


if __name__ == '__main__':
    pass
