
class Apply():
    def __init__(self, owner, operation):
        self.owner = owner
        self.operation = operation
        self.candidates = []

    def arbitrate(self):
        print(f"MPU{self.owner.get_id()}.Apply: Arbitrating to pick a candidate.")
        candidate = self.candidates.pop(0)
        print(f"MPU{self.owner.get_id()}.Apply: Picked candidate with vid {candidate}.")
        if candidate != None:
            print(f"MPU{self.owner.get_id()}.Apply: Picked candidate with vid {candidate}.")
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
        print(f"MPU{self.owner.get_id()}.Apply: Received a candidate with vid {vid}.")
        self.candidates.append(vid)
        # NOTE: Currently we call arbitrate as soon as we receive a candidate.
        # This is due to the fact that in this simulation we don't have any
        # notion of time.
        self.arbitrate()

    def send_work(self, edges, new_prop):
        self.owner.recv_work(self, edges, new_prop)
