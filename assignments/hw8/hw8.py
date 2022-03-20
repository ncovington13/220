"""
Nia Covington
hw8.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>
I certify that this assignment is entirely my own work.
"""

import math
from graphics import *

def add_ten(nums):
    nums[:]=[i +10 for i in nums]

def square_each(nums):
    for i in range(len(nums)):
        if isinstance(nums[i],int)==True:
            nums[i]=int(nums[i]) **2
        else:
            nums[i]=float(nums[i]) **2
    return nums

def sum_list(nums):
    total: int=0
    for i in nums:
        total+= i
    return total

def to_numbers(nums):
    for i in nums:
        int(i)


def sum_of_squares(nums):
    for i in nums:
        int(i)
    nums[:]=[nums[i] **2 for i in nums]
    acc=1
    for i in range(nums):
        acc+= nums[i] **2
    return nums


def starter(weight, wins):
    if weight >=150 and weight<160 and wins>=5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False

def leap_year(year):
    leap= False
    if year % 400==0:
        leap=True
    elif year %100==0:
        leap=False
    elif year % 4 ==0:
        leap= True
    return leap


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_2=win.getMouse()
    circumference_point_2= win.getMouse()
    radius_2 = math.sqrt(
        (center_2.getX() - circumference_point_2.getX()) ** 2 + (center_2.getY() - circumference_point_2.getY()) ** 2)
    circle_two = Circle(center_2, radius_2)
    circle_two.setFill('green')
    circle_two.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    radius_2 = math.sqrt(
        (center_2.getX() - circumference_point_2.getX()) ** 2 + (center_2.getY() - circumference_point_2.getY()) ** 2)
    circle_two = Circle(center_2, radius_2)
    circle_two.setFill('green')
    circle_two.draw(win)

    x_formula=abs((circle_one).getCenter().getX()-circle_two.getCenter().getX()**2)
    y_formula=abs((circle_one.getCenter().getY()-circle_two.getCenter().getY())**2)
    distance=math.sqrt(x_formula + y_formula)
    if distance < 0:
        msg=Point((100,300),"The circles overlap")
        msg.draw(win)
    else:
        msg2=Point((50,350),"The circles do not overlap")
        msg2.draw(win)

    close=Text((Point(250,600),"Click anywhere to close!"))
    close.setSize(20)
    close.draw(win)
    win.getMouse()
    win.close()

did_overlap()


if __name__ == '__main__':
    pass
