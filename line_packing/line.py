import math
from numba import njit

class Line:
    @staticmethod
    def from_point_slope(x, y, m, l):
        return Line(x - l/2, y - (m*l)/2, x + l/2, y + (m*l)/2)

    def __init__(self, x_1, y_1, x_2, y_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2
        self.width = self.calculate_width()

    def intersects(self, other):
        def do_segments_intersect_unordered(x1, y1, x2, y2, x3, y3, x4, y4):
            # Check if the line segments have any common points
            if (x1, y1) == (x3, y3) or (x1, y1) == (x4, y4) or (x2, y2) == (x3, y3) or (x2, y2) == (x4, y4):
                return True
            
            # Calculate the direction vectors of the line segments
            dx1 = x2 - x1
            dy1 = y2 - y1
            dx2 = x4 - x3
            dy2 = y4 - y3
            
            # Calculate the determinant
            det = dx1 * dy2 - dx2 * dy1
            
            # Check if the line segments are parallel (det == 0)
            if det == 0:
                return False
            
            # Calculate parameters for both segments
            t = (dx2 * (y1 - y3) - dy2 * (x1 - x3)) / det
            s = (dx1 * (y1 - y3) - dy1 * (x1 - x3)) / det

            # Check if the intersection point is within both segments
            if 0 <= t <= 1 and 0 <= s <= 1:
                return True

            return False
        return do_segments_intersect_unordered(self.x_1, self.y_1, self.x_2, self.y_2, other.x_1, other.y_1, other.x_2, other.y_2)

    
    def out_of_bounds(self, width, height):
        buffer = self.width * 2
        min_x = min(self.x_1, self.x_2)
        max_x = max(self.x_1, self.x_2)
        min_y = min(self.y_1, self.y_2)
        max_y = max(self.y_1, self.y_2)
        return min_x - buffer < 0 or max_x + buffer > width or min_y - buffer < 0 or max_y + buffer > height
    
    def calculate_width(self) -> int:
        d_sqr = abs(self.x_1 - self.x_2) + abs(self.y_1 - self.y_2)
        return int(d_sqr * 0.03)
    
    def __repr__(self) -> str:
        return f'Line ({self.x_1}, {self.y_1}), ({self.x_2}, {self.y_2})'