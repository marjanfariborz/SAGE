class WorkListItem():
    def __init__(self, vid, temp_prop, prop, valid):
        self.vid = vid
        self.temp_prop = temp_prop
        self.prop = prop
        self.valid = valid

    def get_id(self):
        return self.vid

    def get_temp_prop(self):
        return self.temp_prop

    def set_temp_prop(self, temp_prop):
        self.temp_prop = temp_prop

    def get_prop(self):
        return self.prop

    def set_prop(self, prop):
        self.prop = prop

    def is_valid(self):
        return self.valid

    def validate(self):
        self.valid = True

    def invalidate(self):
        self.valid = False

    def __str__(self):
        ret = f"WorkListItem[vid={self.vid}, temp_prop={self.temp_prop}, prop={self.prop}, valid={self.valid}]"
        return ret

    def __repr__(self):
        return str(self)
