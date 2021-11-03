from graph_reader import Vertex

class Apply():
    def __init__(self, owner, operation):
        self.owner = owner
        self.operation = operation
        self.candidates = []

    def arbitrate(self):
        candidate = self.candidates.pop(0)
        if candidate != None:
            work_list_item = self.owner.read_work_list_item(candidate)
            assert work_list_item.is_valid()
            temp_prop = work_list_item.get_temp_prop()
            prop = work_list_item.get_prop()
            new_prop = self.operation(temp_prop, prop)
            # TODO: Talk to Marjan about this
            # work_list_item.invalidate()
            if new_prop != prop:
                work_list_item.set_prop(new_prop)
                self.owner.write_work_list_item(candidate, work_list_item)
                edges = self.owner.read_edge_list(candidate)
                self.send_work(edges, new_prop)

    def recv_candidate(self, vid):
        self.candidates.append(vid)

    def send_work(self, edges, new_prop):
        self.owner.recv_work(self, edges, new_prop)
