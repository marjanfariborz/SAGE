

class Push():
    def __init__(self, owner, operation):
        self.owner = owner
        self.operation = operation
        self.localQ = []
        self.globalQ = []

    def recv_update(self, edges, temp_prop):
        self.owner.read_apply()
        self.value = temp_prop
        self.weight = edges.get_weight()
        self.vid = edges.get_neighbor()
        self.push(self)

    def send_update(self, vid, value):
        if (vid % 2) == self.owner.get_id():
            self.localQ.append({vid, value})
        else:
            self.globalQ.append({vid, value})

    def push(self):
        propagate = self.operation
        new_value = propagate(self.value, self.weight)
        self.send_update(self.vid, new_value)


