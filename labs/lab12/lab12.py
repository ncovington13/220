"""
Nia Covington
lab12.py
Create programs using while control structures and python functions.
I certify this is my own work.
"""

from random import randint
def find_and_remove_first(list,value):
    i=0
    repeat=0
    while i <= len(list):
        if list[i]==value and repeat==0:
            list.remove(value)
            list.insert(i,'Nia')
            repeat=repeat+1
        i=i+1


def read_file(filename):
    values=[]
    i=0
    file=open(filename,"r")
    r_file=file.readlines()
    while r_file:
        a

def is_in_linear(search_val,values):
    if search_val in values:
        return True
    return False

def good_input():
    n=int(input("Enter number:"))
    while n <1 or n>10:
        if n<1:
            print("Number is too low, should be greater than 0. Try again!")
        else:
            print("Number is too high, should be less than 10. Try again!")
        n=int(input("Enter number:"))

    return "good input"

def num_digits():
   prompt=int(input("Please input a positive interger"))
   count=0
   while prompt !=0:
       prompt//=10
       count+=1
   print("Number of digits:"+str(count))

def hi_lo_game():
    number=randint(1,100)
    i=0
    while i <=7:
        prompt=int(input("Please guess the number:"))
        if number== prompt:
            print("Correct \n" "You win in",i+1,"guesses!")
            continue
        elif prompt>number:
            print("too high")
        elif prompt < number:
            print("too low")
        else:
            print("Sorry, you lose. The number was",number)


if __name__=="__main__":
    print("Testing function")
    print(good_input())
    num_digits()
    hi_lo_game()