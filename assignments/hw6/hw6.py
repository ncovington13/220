"""
Nia Covington
stringformatting.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

I certify that this assignment is entirely my own work.
"""
import math

from math import *
def cash_converter():
    user_input=eval(input("enter an integer:"))
    print("that is ${:.2f}".format(user_input))

def encode():
    message=input("Enter a message:")
    key=eval(input("Enter a key:"))
    answer="".join(chr(ord(c)+ key) for c in message)
    print(answer)

def sphere_area(radius):
    area= float(4 * math.pi * (radius)**2)
    return area

def sphere_volume(radius):
    volume= float((4/3) * math.pi *(radius)**3)
    return volume

def sum_n(number):
    sum=0
    for i in range(1,number+1):
        sum+= i
    return sum

def sum_n_cubes(number):
    cubes_sum=0
    for i in range (1,number+1):
        cubes_sum+=(i**3)
    return cubes_sum


def encode_better():
    user_message=input("Enter a word:")
    user_key=input("Enter a key:")
    shift_list=[]
    chr_list=[]

    answer=""
    # answer will print as a string rather than a list
    for keys in user_key:
        shift_list.append(keys)
    for ch in user_message:
        chr_list.append(ch)

    for i in range(len(user_message)):
        shift= (ord(shift_list [i % len(shift_list)])-65) % 58
        answer += chr((ord(chr_list[i])+ shift -58))
    print(answer)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
