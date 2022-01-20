"""
Name: Nia Covington
assignment 1.py

Problem: <This program is used to learn how to use Python and create simple arithmetic equations for an output. >

Certification of Authenticity: I certify that this is entirely my own work.
"""


def calc_rec_area():
    length= eval(input("Enter the length:"))
    width= eval(input("Enter the width:"))
    area=length* width
    # represents the formula that gives area
    print("Area=", area)
calc_rec_area()


def calc_volume():
    length= eval(input("Enter the length:"))
    width= eval(input("Enter the width:"))
    height= eval(input("Enter the height:"))
    volume= length*width*height
   # represent the formula for volume
    print("Volume=", volume)
calc_volume()


def shooting_percentage():
    total_shots= eval(input("Enter the player's total number of shots:"))
    shots_made= eval(input("Enter how many shots the player made:"))
    fg_percentage=(shots_made/total_shots)*100
    # represents the ratio for the shooting percentage
    print("Shooting Percentage=",fg_percentage, "%")
shooting_percentage()


def coffee():
    pounds= eval(input("How many pounds of coffee would you like?"))
    total= 10.50*pounds +0.86*pounds + 1.50
    # represents the formula for calculating the total
    print("Your total is","$", total)
coffee()

def kilometers_to_miles():
    kilometers= eval(input("How many kilometers did you travel?"))
    miles=0.6213*kilometers
    # represents the conversion equation
    print("That's",miles,"miles!",end="\n")
kilometers_to_miles()

if __name__ == '__main__':
    pass
