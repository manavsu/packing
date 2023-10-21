
class circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def intersects(self, other, buffer=0):
        return (self.x - other.x)**2 + (self.y - other.y)**2 <= (self.r + other.r + buffer)**2
    
    def out_of_bounds(self, width, height, buffer):
        return self.x - self.r - buffer < 0 or self.x + self.r + buffer > width or self.y - self.r - buffer < 0 or self.y + self.r + buffer > height