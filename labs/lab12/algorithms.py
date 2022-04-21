"""
Nia Covington
algorithms.py
Create different algorithms to figure out problems.
I certify this is my own work.
"""
from graphics import *
def read_data(filename):
    file=open(filename,"r")
    read=file.readline()
    split=read.split()
    i=0
    list= []
    while read:
        while i <len(split):
            num=eval(split[i])
            list.append(num)
            i +=1
        read=file.readline()
        split=read.split()
    return list

def is_in_linear(search_val,values):
    if search_val in values:
        return True
    else:
        return False

def selection_sort(values):
    for i in range(len(values)):
        minimum= i
        for j in range(i,len(values)):
            if values[minimum] > values[j]:
                minimum=j
        list[minimum],list[i]=list[i],list[minimum]

def calc_area(rect):
    point_1=rect.getP1()
    point_2=rect.getP2()
    x_p1=point_1.getX()
    x_p2=point_2.getX()
    y_p1=point_1.getY()
    y_p2=point_2.getY()
    side=abs((x_p2-x_p1))
    side2=abs((y_p2-y_p1))
    formula= side * side2
    return formula

def rect_sort(rectangles):
    for i in range(len(rectangles)):
        minimum=i
        for j in range(i,len(rectangles)):
            if calc_area(rectangles[minimum]) > calc_area(rectangles[j]):
                minimum=j
        rectangles[minimum],rectangles[i]=rectangles[i],rectangles[minimum]
