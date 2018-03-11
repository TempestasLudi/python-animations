from lib.Interpolation import Interpolation
from lib.animations.animation import Animation
from lib.animations.value_animation import ValueAnimation
from lib.data.interval import Interval
from lib.data.property import Property


class Translation(Animation):
    def __init__(self, interval, vector, obj, interpolation_function=Interpolation.linear):
        super().__init__(interval)
        self.vector = vector
        self.object = obj
        self.interpolation_function = interpolation_function

    def init(self, obj=None):
        if obj is None:
            obj = self.obj

        return [ValueAnimation(
            self.interval,
            Interval(obj[i], obj[i] + self.vector[i]),
            Property(obj, i),
            self.interpolation_function
        ) for i in [0, 1]]
