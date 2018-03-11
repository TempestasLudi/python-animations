from lib.shapes.animated_shape import AnimatedShape
from matplotlib.patches import Circle

from lib.point import Point


class AnimatedGrid(AnimatedShape):
    def __init__(self, center, size, spacing, point_radius=.01):
        super().__init__()
        self.center = center
        self.size = size if type(size) == tuple else (size, size)
        self.spacing = spacing if type(spacing) == tuple else (spacing, spacing)
        self.objects = [Point(
            i * self.spacing[0] - self.spacing[0] * (self.size[0] - 1) / 2 + self.center[0],
            j * self.spacing[1] - self.spacing[1] * (self.size[1] - 1) / 2 + self.center[1])
            for i in range(self.size[0]) for j in range(self.size[1])]
        self.artists = [Circle(point, point_radius) for point in self.objects]
