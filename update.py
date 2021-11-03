
class Update():
    def __init__(self, vid, value, weight):
        self.vid = vid
        self.value = value
        self.weight = weight

    def get_vid(self):
        return self.vid

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        return f"Update[vid={self.vid}, value={self.value}, weight={self.weight}]"

    def __repr__(self):
        return str(self)
