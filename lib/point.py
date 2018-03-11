import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        raise IndexError(key + " point index out of range")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
            return
        if key == 1:
            self.y = value
            return
        raise IndexError(key + " point index out of range")

    def __sub__(self, other):
        return Point(self[0] - other[0], self[1] - other[1])

    def __add__(self, other):
        return Point(self[0] + other[0], self[1] + other[1])

    def get_r(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def set_r(self, r):
        current = self.get_r()
        if current > 0:
            self.x *= r / current
            self.y *= r / current

    def get_theta(self):
        return math.atan2(self.y, self.x)

    def set_theta(self, theta):
        diff = theta - self.get_theta()
        (self.x, self.y) = (
            math.cos(diff) * self.x - math.sin(diff) * self.y,
            math.cos(diff) * self.y + math.sin(diff) * self.x
        )

    r = property(get_r, set_r)
    theta = property(get_theta, set_theta)
