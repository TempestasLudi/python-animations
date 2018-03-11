from lib.Interpolation import Interpolation
from lib.animations.animation import Animation


class ValueAnimation(Animation):
    def __init__(self, time_interval, value_interval, animated_property, interpolation_function=Interpolation.linear):
        super().__init__(time_interval)
        self.property = animated_property
        self.interpolation = Interpolation(time_interval, value_interval, interpolation_function)

    def update(self, t):
        self.property.set(self.interpolation.interpolate(t))
