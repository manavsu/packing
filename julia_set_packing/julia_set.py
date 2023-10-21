import numpy as np
from numba import njit

"""
pass in square np array, and fill in array with julia set centered at c.
only fill in if the canvas is all background for a given array + buffer
"""
class JuliaSet:
    def __init__(self, x, y, l):
        self.x = x
        self.y = y
        self.l = l

    def populate(self, c):
        #Fill in np array of with the julia se
        pass

    @njit
    def canvas_empty(self, canvas, background):
        if (canvas != background).any():
            return False
        return True
    
    def out_of_bounds(self, width, height, buffer):
        return self.x + self.l + buffer > width or self.x - self.l - buffer < 0 or self.y + self.l + buffer > height or self.y - self.l - buffer < 0
    
    def outline_width(self) -> int:
        radius = self.r
        if radius < 300:
            return int(radius * 0.1)
        if radius < 600:
            return int(radius * 0.05)
        return int(radius * 0.03)