from lib.animation_initializers.initializer import Initializer


class GroupAnimation(Initializer):
    def __init__(self, objects, initializer):
        super().__init__(initializer.interval)
        self.objects = objects
        self.initializer = initializer
        self.animations = []

    def init(self, obj=None):
        if obj is None:
            return [a for o in self.objects for a in self.initializer.init(o)]
        else:
            return self.initializer.init(obj)
