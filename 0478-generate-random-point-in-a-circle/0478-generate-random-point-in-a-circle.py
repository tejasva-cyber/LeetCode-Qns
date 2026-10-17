import random
import math

class Solution:

    def __init__(self, radius, x_center, y_center):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        angle = random.random() * 2 * math.pi
        distance = self.r * math.sqrt(random.random())

        return [
            self.x + distance * math.cos(angle),
            self.y + distance * math.sin(angle)
        ]