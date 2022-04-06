"""
Nia Covington
door.py
Create a user defined class using a list of objects.
I certify this is my own work.
"""

from graphics import *
class Door:
    def __init__(self,shape,label):
        self.shape=shape
        door_position=shape.getCenter()
        self.text=Text(door_position,label)
        self.secret=False
    def get_label(self):
        return self.text.getText()
    def set_label(self,label):
        self.text.setText(label)
    def draw(self,win):
        self.shape.draw(win)
        self.text.draw(win)
    def undraw(self):
        self.shape.undraw()
        self.text.undraw()
    def is_clicked(self,point):
        p1_x=self.shape.getP1().getX()
        p2_x=self.shape.getP2().getX()
        p1_y=self.shape.getP1().getY()
        p2_y=self.shape.getP2().getY()
        if p1_x <= point.getX() <= p2_x  and p1_y<= point.getY() <= p2_y:
            return True
        else:
            return False
    def open(self,color,label):
        self.shape.setFill(color)
        self.text.setText(label)
    def close(self,color,label):
        self.shape.setFill(color)
        self.text.setText(label)
    def color_door(self,color):
        self.shape.setFill(color)
    def is_secret(self):
        return self.secret
    def set_secret(self,secret):
        self.secret=secret




