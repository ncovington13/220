"""
Nia Covington
lab8.py
Joyride Bumpers
I cerify this is my own work.
"""
import math
from random import randint
from graphics import *
def get_random(move_amount):
    return randint(-move_amount,move_amount)

def did_collide(ball,ball_2):
    x_formula=abs((ball.getCenter().getX()-ball_2.getCenter().getX())**2)
    y_formula=abs((ball.getCenter().getY()- ball_2.getCenter().getY())**2)
    distance= math.sqrt((x_formula)+(y_formula))
    if distance > ball.getRadius() + ball_2.getRadius():
        return False
    else:
        return True

def hit_vertical(ball,win):
    bottom=win.getHeight()
    top_formula= ball.getCenter().getY()-ball.getRadius()
    bottom_formula=ball.getCenter().getY()+ ball.getRadius()
    if top_formula < 0 or bottom_formula > bottom:
        return True
    else:
        return False

def hit_horizontal(ball,win):
    right=win.getWidth()
    left_formula= ball.getCenter().getX()-ball.getRadius()
    right_form=ball.getCenter().getX() + ball.getRadius()
    if left_formula < 0 or right_form > right:
        return True
    else:
        return False

def get_random_color():
    r_value= randint(0,255)
    g_value=randint(0,255)
    b_value=randint(0,255)
    return color_rgb(r_value,g_value,b_value)

def bumper():
    win_width=400
    win_height=400
    win=GraphWin("Bumper",win_width,win_height)
    # creates a window
    circ_1=Circle(Point(randint(0,400), randint(0,400)),25)
    circ_2=Circle(Point(randint(0,400),randint(0,400)),25)
    circ_1.setFill(get_random_color())
    circ_2.setFill(get_random_color())
    circ_1.draw(win)
    circ_2.draw(win)
    # creates the bumper cars
    movement_x_1=get_random(20)
    movement_y_1=get_random(35)
    movement_x_2=get_random(20)
    movement_y_2=get_random(35)
    while not win.checkMouse():
        time.sleep(0.2)
        circ_1_move = circ_1.move(movement_x_1, movement_y_1)
        circ_2_move = circ_2.move(movement_x_2, movement_y_2)
        # in order to make sure the balls don't bounce
        if hit_vertical(circ_1,win):
            movement_y_1=-movement_y_1
        if hit_vertical(circ_2,win):
            movement_y_2= -movement_y_2
        if hit_horizontal(circ_1,win):
            movement_x_1=-movement_x_1
        if hit_horizontal(circ_2,win):
            movement_x_2=-movement_x_2
        if did_collide(circ_1,circ_2):
            movement_x_1=-movement_x_1
            movement_x_2=-movement_x_2
            movement_y_1=-movement_y_1
            movement_y_2=-movement_y_2
    else:
        win.close()
bumper()

