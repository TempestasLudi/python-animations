import math


class Interpolation:
    def __init__(self, time_interval, value_interval, func):
        self.time_interval = time_interval
        self.value_interval = value_interval
        self.function = func

    def interpolate(self, t):
        y = self.function(t / self.time_interval.length)
        return self.value_interval.start + self.value_interval.length * y

    @staticmethod
    def linear(t):
        return t

    @staticmethod
    def cubic(t):
        return -2 * math.pow(t, 3) + 3 * math.pow(t, 2)

    @staticmethod
    def quintic(t):
        return 6 * math.pow(t, 5) - 15 * math.pow(t, 4) + 10 * math.pow(t, 3)

    @staticmethod
    def septic(t):
        return -20 * math.pow(t, 7) + 70 * math.pow(t, 6) - 84 * math.pow(t, 5) + 35 * math.pow(t, 4)

    @staticmethod
    def sine(t):
        return .5 - math.cos(t * math.pi) / 2
