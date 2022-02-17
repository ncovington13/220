"""
Nia Covington
lab5.py
Graphics and Strings
Create a program that performs certain functions in graphics and using strings.
I certify that this is my own work.
"""


from graphics import *
from math import *
def triangle():
    win=GraphWin("Triangle", 500, 500)
    # create a graphical window

    open_message=Text(Point(250,450), "Click mouse three times in window")
    open_message.setStyle("bold")
    open_message.setSize(14)
    open_message.draw(win)
    # prompt that allows them to pick points for

    p1=win.getMouse()
    p1.draw(win)
    p2=win.getMouse()
    p2.draw(win)
    p3=win.getMouse()
    p3.draw(win)
    open_message.undraw()
    # points for the triangle
    tri_shape=Polygon(p1,p2,p3)
    tri_shape.draw(win)
    tri_shape.setFill('blue')
    tri_shape.setOutline('white')

    p1_x=abs(p1.getX()-p2.getX())
    p1_y=abs(p1.getY()-p2.getY())
    leng1=sqrt((p1_x)**2 + (p1_y)**2)
    p2_x=abs(p2.getX()-p3.getX())
    p2_y=abs(p2.getY()-p3.getY())
    leng2=sqrt((p2_x)**2 + (p2_y)**2)
    p3_x=abs(p3.getX()-p1.getX())
    p3_y=abs(p3.getY()-p1.getY())
    leng3=sqrt((p3_x)**2 + (p3_y)**2)
    peri= leng1+leng2+leng3
    per_message=Text(Point(200,50), "Perimeter:" +str(peri))
    per_message.setTextColor('white')
    per_message.draw(win)


    s= (leng1 + leng2 + leng3)/2
    area=sqrt((s)*(s-leng1)*(s-leng2)*(s-leng3))
    area_message=Text(Point(200,100),"Area:" +str(area))
    area_message.setTextColor('white')
    area_message.draw(win)
# displays both the area and perimeter
    end_message=Text(Point(100,450),"Click to close!")
    end_message.setStyle('bold')
    end_message.setSize(14)
    end_message.setTextColor('white')
    end_message.draw(win)
    win.getMouse()
    win.close()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    r=Entry(Point(255,240),3)
    r.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    g=Entry(Point(255,270),3)
    g.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    b=Entry(Point(255,300),3)
    b.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        r_value=eval(r.getText())
        b_value=eval(b.getText())
        g_value=eval(g.getText())
        shape.setFill(color_rgb(r_value,g_value,b_value))

    # Wait for another click to exit
    close_inst=Text(Point(150,25),"Click to close!")
    close_inst.draw(win)
    win.getMouse()
    win.close()

def process_string():
    user_string=input("enter a string")
    print(user_string[0])
    print(user_string[-1])
    print(user_string[2:6])
    print(user_string[0]+user_string[-1])
    print(10 * user_string[:3])
    for i in user_string:
        print(i)
    print(len(user_string))

def process_list():
    pt = Point(5,10)
    values= [5,"hi",2.5,'there', pt, '7.2']
    x= values[1]+values[3]
    print(x)
    x=values[0]+values[2]
    print(x)
    x= values[1] * 5
    print(x)
    x=values[2:5]
    print(x)
    x=values[2:4]+[values[0]]
    print(x)
    x=[values[2]]+[values[0]]+[values[5]]
    print(x)
    x=values[0]+values[2]+7.2
    print(x)
    x=len(values)
    print(x)

def another_series():
    terms = eval(input("How many terms?"))
    acc_total=0
    my_list = [246]
    for i in range(terms):
        x= 2+ (2 * (i % 3))
        print(x, end=" ")
        acc_total=acc_total+x
    print()
    print("sum", acc_total)
another_series()
def target():
    win=GraphWin("Target",300,300)
    center=Point(150,150)

    white_circ=Circle(center,100)
    white_circ.setFill('white')
    white_circ.draw(win)
    # drawing white circle

    bla_circle=Circle(center,80)
    bla_circle.setFill('black')
    bla_circle.draw(win)

    blue_circle=Circle(center,60)
    blue_circle.setFill('blue')
    blue_circle.draw(win)

    red_circ=Circle(center,40)
    red_circ.setFill('red')
    red_circ.draw(win)

    yellow_circ=Circle(center,20)
    yellow_circ.setFill('yellow')
    yellow_circ.draw(win)

    instruct=Text(Point(125,275),"Click to close!")
    instruct.setStyle('bold')
    instruct.draw(win)
    win.getMouse()
    win.close()

