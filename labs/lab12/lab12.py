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
    while i < len(list):
        if list[i]==value and repeat==0:
            list.remove(value)
            list.insert(i,'Nia')
            repeat=repeat+1
        i=i+1

def good_input():
    user=eval(input("Enter number 1-10:"))
    while user >=0 or user <=11:
        if user<1:
            print("Number is too low.")
            user=eval(input('Enter a number 1-10:'))
        elif user >10:
            print("Number is too high.")
            user=eval(input("Enter a number 1-10:"))
        else:
            return user

    return "good input"

def num_digits():
   prompt= eval(input('Enter a positive integer:'))
   count=0
   while prompt !=0:
       count= count + 1
       prompt //= 10
   print("Number of digits:", count)

def hi_lo_game():
    number=randint(1,100)
    i=0
    switch=False
    while i !=7 and switch==False:
        prompt=int(input("Please guess the number:"))
        if prompt> number:
            i+=1
            print("too high")
        elif prompt< number:
            i+=1
            print("too low")
        else:
            switch=True
            i +=1
            print("You win in {} guesses".format(i))
    else:
        if i==7:
            print("Sorry, you lose. The number was {}".format(number))

if __name__=="__main__":
    print(good_input())
    num_digits()
    hi_lo_game()