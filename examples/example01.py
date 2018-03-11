import math

from matplotlib import patches

from lib.Interpolation import Interpolation
from lib.data.interval import Interval
from lib.data.options import Options
from lib.data.property import Property
from lib.movie import Movie
from lib.scene import Scene
from lib.shapes.animated_grid import AnimatedGrid
from lib.animation_initializers.value_animation import ValueAnimation

# Create a new movie with one scene
movie = Movie()
scene = Scene()
movie.scenes.append(scene)

# Create a grid with center (0, 0), with 30 points in each direction that are .05 apart
grid = AnimatedGrid((0, 0), 30, .05)

# Add the visible parts of the grid to the scene
scene.add_artists(grid.artists)

# Add a circle (the "unit circle") to the scene
scene.add_artists([patches.Circle((0, 0), .5, facecolor='None')])

interpolation = Interpolation.quintic

# Add an animation of the theta parameters of the points in the grid to the scene (rotate every point pi radians with
#  respect to the origin)
scene.initializers.append(grid.animate(ValueAnimation(Interval(0, 2), math.pi, Property(None, "theta"), interpolation)))

# Add an animation of the r parameters of the points in the grid to the scene (move every point to the square root of
#  its distance to the origin)
scene.initializers.append(grid.animate(ValueAnimation(Interval(2, 4), lambda p: math.sqrt(p.r / 2) - p.r,
                                                      Property(None, "r"), interpolation)))

# Export the movie with a quality of 720p
movie.bake(Options.presets["720p"])
