from lib.Interpolation import Interpolation
from lib.animation_initializers.initializer import Initializer
import lib.animations.value_animation as value_animation
from lib.data.interval import Interval


class ValueAnimation(Initializer):
    def __init__(self, interval, difference_function, animated_property, interpolation_function=Interpolation.linear):
        super().__init__(interval)
        self.difference_function = difference_function
        if not callable(self.difference_function):
            self.difference_function = lambda o: difference_function

        self.property = animated_property
        self.interpolation_function = interpolation_function

    def init(self, obj=None):
        if obj is None:
            animated_property = self.property
        else:
            animated_property = self.property.clone(obj)

        current = animated_property.get()

        return [value_animation.ValueAnimation(
            self.interval,
            Interval(current, current + self.difference_function(obj)),
            animated_property,
            self.interpolation_function
        )]
