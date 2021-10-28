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
            if work_list_item.is_valid():
                vid = work_list_item.get_vid()
                temp_prop = work_list_item.get_temp_prop()
                prop = work_list_item.get_prop()
                prop_n = self.operation(temp_prop, prop)
                work_list_item.invalidate()
                if prop_n != prop:
                    work_list_item.set_prop(prop_n)
                    self.owner.write_work_list_item(work_list_item)
                    edges = self.owner.read_edge_list(vid)
                    # TODO: Call Push for edges and prop
