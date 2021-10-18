
class ReduceWL():
    def __init__(self,  op = max, vid, vntp):
        self.op = op
        self.vertex = vid
        self.nvtp = vntp
    def read_wl(self):
        ' vtp, vp, active = send_WL(self.vid)'
        'self.reduce(valid, vtp)'
    def redue(self, valid, vtp):
        if valid:
            ' op(vtp, self.nvtp)'
        else:
            ' vtp = op(vp, nvtp )'
            valid =1
        self.write_wl(vid, vtp, valid)

    def write_wl(self, vtp, valid):
        # WL(Vid) = vtp, valid
