from anything import Anything

class ApplyStats():
    def __init__(self):
        self.num_worklist_reads = 0
        self.num_worklist_writes = 0
        self.num_edges_read = 0
        # TODO: Add this stats after figuring out placing vertices
        # based on address
        self.num_edge_bytes_read = 0

    def get_dict(self):
        return self.__dict__

class Apply(Anything):
    def __init__(self, owner, aid, operation, debug_print=False):
        super().__init__(owner, aid, debug_print)
        self.set_name()
        self.operation = operation
        self.candidates = []
        self.stats = ApplyStats()

    def arbitrate(self):
        self.print_debug("Arbitrating to pick a candidate.")
        candidate = self.candidates.pop(0)
        self.print_debug(f"Picked candidate with vid {candidate}.")
        if candidate != None:
            self.print_debug(f"Picked candidate with vid {candidate}.")
            self.print_debug("Reading the proper WorkListItem.")
            work_list_item = self.owner.read_work_list_item(candidate)
            self.stats.num_worklist_reads += 1
            self.print_debug(f"Read the WorkListItem for vid {candidate}.\nWorkListItem: {work_list_item}")
            self.print_debug(f"Checking validity of WorkListItem.")
            assert work_list_item.is_valid()
            self.print_debug("Assertion passed.")
            temp_prop = work_list_item.get_temp_prop()
            prop = work_list_item.get_prop()
            self.print_debug(f"Reducing with temp_prop = {temp_prop}, prop = {prop}.")
            new_prop = self.operation(temp_prop, prop)
            # TODO: Talk to Marjan about this
            work_list_item.invalidate()
            if new_prop != prop:
                self.print_debug(f"Prop for vid {candidate} has changed.")
                work_list_item.set_prop(new_prop)
                self.print_debug(f"Updating the WorkListItem for vid {candidate}")
                self.owner.write_work_list_item(candidate, work_list_item)
                self.stats.num_worklist_writes += 1
                self.print_debug(f"Reading the EdgeList for vid {candidate}")
                edges = self.owner.read_edge_list(candidate)
                self.stats.num_edges_read += len(edges)
                self.print_debug(f"Read the EdgeList for vid {candidate}.\nEdgeList: {edges}")
                self.print_debug(f"Sending work to Push with new_prop = {new_prop}.\nEdgeList: {edges}")
                self.send_work(edges, new_prop)

    def recv_candidate(self, vid):
        self.print_debug(f"Received a candidate with vid {vid}.")
        self.candidates.append(vid)
        # NOTE: Currently we call arbitrate as soon as we receive a candidate.
        # This is due to the fact that in this simulation we don't have any
        # notion of time.
        self.arbitrate()

    def send_work(self, edges, new_prop):
        self.owner.recv_work(edges, new_prop)

    def get_stats(self):
        meta_data = {"name": self.name}
        stats = self.stats.get_dict()
        meta_data.update(stats)
        ret = meta_data
        return ret
