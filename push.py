from update import Update
from anything import Anything

class Push(Anything):
    def __init__(self, owner, pid, operation, debug_print=False):
        super().__init__(owner, pid, debug_print)
        self.set_name()
        self.operation = operation

    def recv_work(self, edges, new_prop):
        self.print_debug(f"Received new work with new_prop = {new_prop}.\nEdgeList: {edges}")
        updates = []
        self.print_debug(f"Creating new updates based on new_prop {new_prop}")
        for edge in edges:
            self.print_debug(f"Calculating the value for update based on new_prop {new_prop} and edge weight {edge.get_weight()}.")
            value = self.operation(new_prop, edge.get_weight())
            self.print_debug(f"Calculated value {value} based on new_prop {new_prop} and edge weight {edge.get_weight()}")
            update = Update(edge.get_neighbor(), value)
            self.print_debug(f"Created new update {update}")
            updates.append(update)
        self.print_debug(f"Sending updates.\nupdates: {updates}")
        self.send_updates(updates)

    def send_updates(self, updates):
        self.print_debug(f"Sending new updates to network {updates}")
        self.owner.recv_updates(updates)
