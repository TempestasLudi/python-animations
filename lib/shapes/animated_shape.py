from lib.animation_initializers.group_animation import GroupAnimation


class AnimatedShape:
    def __init__(self):
        self.objects = []
        self.artists = []

    def animate(self, initializer):
        return GroupAnimation(self.objects, initializer)
