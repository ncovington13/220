"""
Nia Covington
lab10.py
Create a user defined class using a list of objects.
I certify this is my own work.
"""

from door import Door
from button import Button
from graphics import *
def main():
    win=GraphWin("Lab 10", 600,600)
    button = Button(Rectangle, "Exit")
    button.draw(win)
    door= Door(Rectangle, "Closed")
    door.color_door('red')
    door.draw(win)
    click= win.getMouse()
    while not click.button.is_clicked(click):
        if door.is_clicked(click):
            return door.open('white','open')
        elif door.is_clicked(click):
            return door.open('red', 'closed')
        click=win.getMouse()
    if button.is_clicked(click):
        return win.close()


