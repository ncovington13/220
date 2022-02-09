"""
Nia Covington
Greeting Card
Create a greeting card for Valentine's Day using the graphics library!
I certify this is my own work.
"""

import graphics
# variable names indicate location
from graphics import*
def greeting_card():
    win=GraphWin("Heart", 500,500)
    heart_shape=Polygon(Point(250,400),Point(280,350),Point(310,300), Point(340,250),Point(370,200),Point(370,200),
                        Point(340,150),Point(310,100),Point(310,100),Point(280,150),Point(250,200),Point(250,400),
                        Point(220,350),Point(190,300),Point(160,250),Point(130,200),Point(130,200),Point(160,150),
                        Point(190,100),Point(190,100),Point(220,150),Point(250,200))
    heart_shape.draw(win)
    heart_shape.setFill('red')
    heart_shape.setOutline('red')
    win.setBackground('pink')

    message=Text(Point(250,450),"Happy Valentine's Day. May you feel love!")
    message.setSize(18)
    message.setFace("arial")
    message.draw(win)

    arrow_bow=Line(Point(0,250), Point(130,250))
    arrow_bow.draw(win)
    arrow_bow.setArrow("last")
    arrow_bow.setWidth(5)
    for i in range(5):
        arrow_bow.move(100,0)
        time.sleep(0.50)

    click_message=Text(Point(250,250),"Click mouse to close!")
    click_message.setSize(14)
    click_message.setFace("arial")
    click_message.draw(win)
    win.getMouse()
    win.close()
greeting_card()