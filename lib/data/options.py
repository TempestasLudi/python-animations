class Options:
    presets = {}

    def __init__(self, frame_rate=30, dpi=54, bitrate=4 * 1000, codec="libx264", extra_args=('-pix_fmt', 'yuv420p')):
        self.frame_rate = frame_rate
        self.dpi = dpi
        self.bitrate = bitrate
        self.codec = codec
        self.extra_args = extra_args


Options.presets["1080p"] = Options(40, 120, 12 * 1000)
Options.presets["720p"] = Options(40, 80, 75 * 100)
Options.presets["480p"] = Options(30, 54, 4 * 1000)
Options.presets["360p"] = Options(30, 40, 15 * 100)
