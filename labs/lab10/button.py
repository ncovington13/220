"""
Nia Covington
button.py
Create a user defined class using a list of objects.
I certify this is my own work.
"""
from graphics import *
class Button:
    def __init__(self,shape,label):
        self.shape=shape
        label_position= shape.getCenter()
        self.text=Text(label_position,label)
    def get_label(self):
        label= self.text.getText()
        return label
    def set_label(self,label):
        self.text.setText(label)
    def draw(self,win):
        self.shape.draw(win)
        self.text.draw(win)
    def undraw(self):
        self.shape.undraw()
        self.text.undraw()
    def is_clicked(self,point):
        xp1_coords=self.shape.getP1().getX()
        xp2_coords=self.shape.getP2().getX()
        yp1_coords=self.shape.getP1().getY()
        yp2_coords=self.shape.getP1().getY()
        if xp1_coords <= point.getX() <= xp2_coords and yp1_coords <= point.getY() <= yp2_coords:
            return True
        else:
            return False
    def color_button(self,color):
        self.shape.setFill(color)









