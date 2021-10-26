from graph_reader import Vertex

class Apply():
    def __init__(self, owner, op = sum):
        self.owner = owner
        self.op = op
        self.vid = 0

    def arbitrate(self):
        work_list_item = self.owner.read_work_list_item(self.vid)
        if work_list_item.is_valid():
            temp_prop = work_list_item.get_temp_prop()
            prop = work_list_item.get_prop()
            prop_n = self.op(temp_prop, prop)
            work_list_item.invalidate()
            if prop_n != prop:
                work_list_item.set_prop(prop_n)
                # TODO: Add reading the edgelist and push here
        # TODO: add termination condition here
        self.vid = self.vid +1
        self.arbitarte()

        '''
        arbitarte in its local worklist
        finds a vid in worklist with valid =1
        self.vtemp = vtemp
        self.value = value
        '''