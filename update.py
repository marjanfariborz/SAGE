
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
