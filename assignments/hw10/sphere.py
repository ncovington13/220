"""
Nia Covington
sphere.py
Create a geometric sphere.
I certify this is my own work.
"""
import math

class Sphere:
    def __init__(self,radius):
        self.radius=radius
    def get_radius(self):
        return int(self.radius)
    def surface_area(self):
        equation= (4 * math.pi * (self.radius ** 2))
        return float(equation)
    def volume(self):
        v_equation= (4/3 * math.pi *(self.radius ** 3))
        return float(v_equation)
