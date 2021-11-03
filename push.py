from update import Update


class Push():
    def __init__(self, owner, operation):
        self.owner = owner
        self.operation = operation
        self.localQ = []
        self.globalQ = []

    def recv_work(self, edges, new_prop):
        updates = []
        for edge in edges:
            value = self.operation(new_prop, edge.get_weight())
            update = Update(edge.get_neighbor(), value)
            updates.append(update)
        self.send_updates(updates)

    def send_updates(self, updates):
        self.owner.recv_updates(updates)

    # def send_update(self, vid, value):
    #     if (vid % 2) == self.owner.get_id():
    #         self.localQ.append({vid, value})
    #     else:
    #         self.globalQ.append({vid, value})

    # def push(self):
    #     propagate = self.operation
    #     new_value = propagate(self.value, self.weight)
    #     self.send_update(self.vid, new_value)


