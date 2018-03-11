from functools import reduce
import matplotlib.animation as animation
import numpy

from lib.data.interval import Interval


class Scene:
    def __init__(self):
        self.artists = []
        self.initializers = []
        self.animations = []

    def play(self, figure, options):
        interval = self.get_interval()
        initialized = set()

        def animate(frame):
            print("Processing frame " + str(frame))

            t = frame / options.frame_rate
            for a in self.animations:
                if t in a.interval:
                    a.update(t - a.interval.start)
                else:
                    self.animations.remove(a)

            new_animations = []
            for i in self.initializers:
                if i not in initialized and t in i.interval:
                    [new_animations.append(a) for a in i.init()]
                    initialized.add(i)

            self.add_animations(new_animations)
            [a.update(t - a.interval.start) for a in new_animations]

            return self.artists

        return animation.FuncAnimation(
            figure,
            animate,
            numpy.arange(interval.start * options.frame_rate, interval.end * options.frame_rate),
            init_func=lambda: animate(0),
            interval=1000 / options.frame_rate,
            blit=True,
            repeat=False
        )

    def get_interval(self):
        if len(self.initializers) > 0:
            return reduce(lambda a, b: a.merge(b), map(lambda a: a.interval, self.initializers))
        else:
            return Interval(0, 1)

    def add_artists(self, artists):
        [self.artists.append(a) for a in artists]

    def add_animations(self, animations):
        [self.animations.append(a) for a in animations]
