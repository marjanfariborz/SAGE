
class WLEngine():
    def __init__(self, owner, operation):
        self.owner = owner
        self.op = operation

    def recv_update(self, update):
        print(f"MPU{self.owner.get_id()}.WLEngine: Received an update.\nUpdate: {update}")
        work_list_item = self.owner.read_work_list_item(update.get_vid())
        print(f"MPU{self.owner.get_id()}.WLEngine: Read the WorkListItem for vid {update.get_vid()}.\nWorkListItem: {work_list_item}")
        if work_list_item.is_valid():
            print(f"MPU{self.owner.get_id()}.WLEngine: The item is valid.\n")
            vtemp = work_list_item.get_temp_prop()
            print(f"MPU{self.owner.get_id()}.WLEngine: Reducing with value = {update.get_value()}, temp_prop = {work_list_item.get_temp_prop()}")
            vtemp = self.operation(update.get_value(), vtemp)
            print(f"MPU{self.owner.get_id()}.WLEngine: Reduced to new temp_prop = {vtemp}")
            work_list_item.set_temp_prop(vtemp)
        else:
            print(f"MPU{self.owner.get_id()}.WLEngine: The item is not valid.\n")
            print(f"MPU{self.owner.get_id()}.WLEngine: Setting temp_prop to {update.get_value()}\n")
            work_list_item.set_temp_prop(update.get_value())
            work_list_item.validate()
        self.owner.write_work_list_item(work_list_item)
        self.owner.recv_candidate(update.get_vid())
