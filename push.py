from update import Update


class Push():
    def __init__(self, owner, operation):
        self.owner = owner
        self.operation = operation
        self.localQ = []
        self.globalQ = []

    def recv_work(self, edges, new_prop):
        print(f"MPU{self.owner.get_id()}.Push: Received new work with new_prop = {new_prop}.\nEdgeList: {edges}")
        updates = []
        print(f"MPU{self.owner.get_id()}.Push: Creating new updates based on new_prop {new_prop}")
        for edge in edges:
            print(f"MPU{self.owner.get_id()}.Push: Calculating the value for update based on new_prop {new_prop} and edge weight {edge.get_weight()}.")
            value = self.operation(new_prop, edge.get_weight())
            print(f"MPU{self.owner.get_id()}.Push: Calculated value {value} based on new_prop {new_prop} and edge weight {edge.get_weight()}")
            update = Update(edge.get_neighbor(), value)
            print(f"MPU{self.owner.get_id()}.Push: Created new update {update}")
            updates.append(update)
        print(f"MPU{self.owner.get_id()}.Push: Sending new updates to network {updates}")
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


