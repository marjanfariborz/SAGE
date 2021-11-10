from anything import Anything
class WLEngine(Anything):
    def __init__(self, owner, wid, operation, debug_print=False):
        super().__init__(owner, wid, debug_print)
        self.set_name()
        self.operation = operation

    def recv_update(self, update):
        vid = update.get_vid()
        value = update.get_value()
        self.print_debug(f"Received an update.\nUpdate: {update}")
        self.print_debug("Reading the proper WorkListItem.")
        work_list_item = self.owner.read_work_list_item(vid)
        self.print_debug(f"Read the WorkListItem for vid {vid}.\nWorkListItem: {work_list_item}")
        vtemp = work_list_item.get_temp_prop()
        self.print_debug(f"Reducing with value = {value}, temp_prop = {vtemp}.")
        vtemp = self.operation(value, vtemp)
        self.print_debug(f"Reduced to new temp_prop = {vtemp}.")
        work_list_item.set_temp_prop(vtemp)
        self.print_debug(f"Setting valid for WorkListItem.")
        work_list_item.validate()
        self.owner.write_work_list_item(vid, work_list_item)
        self.print_debug("Sending candidate to Apply.")
        self.owner.recv_candidate(vid)
