class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __contains__(self, item):
        return self.start <= item <= self.end

    def get_length(self):
        return self.end - self.start

    def merge(self, other):
        return Interval(min(self.start, other.start), max(self.end, other.end))

    length = property(get_length)
