import matplotlib
import matplotlib.pyplot as pyplot
import matplotlib.animation
import matplotlib.patches
import os


class Movie:
    def __init__(self):
        self.scenes = []

    def bake(self, options):
        figure = pyplot.figure(figsize=(16, 9))
        pyplot.axis([-16 / 9, 16 / 9, -1, 1])
        pyplot.axis('off')
        axes = figure.axes[0]
        figure.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

        writer = matplotlib.animation.writers['ffmpeg'](
            fps=options.frame_rate,
            codec=options.codec,
            bitrate=options.bitrate,
            extra_args=options.extra_args
        )

        directory = "output"
        if not os.path.exists(directory):
            os.makedirs(directory)

        for i, scene in enumerate(self.scenes):
            print("== Scene ", str(i), " ==")

            for artist in scene.artists:
                axes.add_artist(artist)

            animation = scene.play(figure, options)

            animation.save(
                directory + "/scene" + str(i) + ".mp4",
                writer=writer,
                dpi=options.dpi
            )

            for artist in scene.artists:
                artist.remove()
