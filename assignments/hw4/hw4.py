"""
Name: Nia Covington
graphics.py
Create a program that uses and displays python graphics and other assets.
I certify that this assignment is entirely my own work.
"""


from graphics import *
import math

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Squares", 400, 400)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.setSize(18)
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(100, 100),Point(150,150))
    shape.setOutline("purple")
    shape.setFill("purple")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of rectangle
        clone=shape.clone()
        clone.draw(win) #used to create new images while keeping old
        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)

    close_message=Text(Point(200,300),"Click again to close.")
    close_message.setSize(30)
    close_message.setFace("times roman")
    close_message.setStyle("bold")
    close_message.setTextColor("white")
    # what displays before closing window
    close_message.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win=GraphWin("Rectangles",500,500)
    message_click=Text(Point(250,450),"Click to make two point")
    message_click.setSize(14)
    message_click.setStyle("bold")
    message_click.draw(win)

    p1=win.getMouse()
    p1.draw(win)
    p2=win.getMouse()
    p2.draw(win)
    message_click.undraw()
    # creates the actual shape of rectangle
    shape_rect=Rectangle(p1,p2)
    shape_rect.draw(win)
    shape_rect.setFill("green")
    shape_rect.setOutline("white")

    per = (abs(p1.getX()- p2.getX()) * 2) + (abs(p1.getY()-p2.getY())*2)
    area= abs(p1.getX() - p2.getX()) * abs(p1.getY() - p2.getY())

    display_mess=Text(Point(250,425), "Perimeter:"+str(per))
    display_mess.draw(win)
    area_mess=Text(Point(250,450), "Area:"+str(area))
    area_mess.draw(win)

    end_message=Text(Point(100,100),"Click to end the program!")
    end_message.setSize(14)
    end_message.setStyle("bold")
    end_message.draw(win)
    win.getMouse()
    win.close()

def circle():
    win=GraphWin("My Circle",700,700)
    msg1=Text(Point(350,25),"Click two points in the window.")
    msg1.draw(win)

    p1=win.getMouse()
    msg1.undraw()
    p2=win.getMouse()

    r= math.sqrt(pow(p1.getX() - p2.getX(),2)) + pow(p1.getY() - p2.getY(),2)
    # equation used to find radius
    cir=Circle(Point(p1.getX(),p1.getY()),r)
    cir.draw(win)
    cir.setFill("blue")

    msg="Radius:"+str(r)
    msg2=Text(Point(350,45),msg)
    msg2.draw(win)

    msg3=Text(Point(350,25), "Click to close window.")
    msg3.draw(win)
    win.getMouse()
    win.close()

def pi2():
    n=int(input("Enter the number of the terms to sum:"))
    apr=0
    numb=4
    denomin=1
    apr += numb/denomin

    for i in range (1,n):
        denomin += 2
        numb *= -1
        apr +=numb/denomin
    print("PI approximation:" +str(apr))
    accuracy_eq=abs(apr-math.pi)
    print("Accuracy:"+str(accuracy_eq))

if __name__ == '__main__':
    pass
