
class Update():
    def __init__(self, vid, value):
        self.vid = vid
        self.value = value

    def get_vid(self):
        return self.vid

    def get_value(self):
        return self.value

    def __str__(self):
        return f"Update[vid={self.vid}, value={self.value}]"

    def __repr__(self):
        return str(self)
