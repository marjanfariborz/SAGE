
class ReduceWL():
    def __init__(self, owner, operation):
        self.owner = owner
        self.op = operation

    def recv_update(self, update):
        # TODO: check and handle the case where work_list_item doesn't exist in the memory
        work_list_item = self.owner.read_work_list_item(update.get_vid())
        if work_list_item.is_valid():
            vtemp = work_list_item.get_temp_prop()
            vtemp = self.operation(update.get_value(), vtemp)
            work_list_item.set_temp_prop(vtemp)
        else:
            vtemp = work_list_item.get_prop()
            vtemp = self.operation(update.get_value(), vtemp)
            work_list_item.set_temp_prop(vtemp)
            work_list_item.validate()
        self.owner.write_work_list_item(work_list_item)
