
class WLEngine():
    def __init__(self, owner, operation):
        self.owner = owner
        self.operation = operation

    def recv_update(self, update):
        vid = update.get_vid()
        value = update.get_value()
        print(f"MPU{self.owner.get_id()}.WLEngine: Received an update.\nUpdate: {update}")
        print(f"MPU{self.owner.get_id()}.WLEngine: Reading the proper WorkListItem.")
        work_list_item = self.owner.read_work_list_item(vid)
        print(f"MPU{self.owner.get_id()}.WLEngine: Read the WorkListItem for vid {vid}.\nWorkListItem: {work_list_item}")
        vtemp = work_list_item.get_temp_prop()
        print(f"MPU{self.owner.get_id()}.WLEngine: Reducing with value = {value}, temp_prop = {vtemp}.")
        vtemp = self.operation(value, vtemp)
        print(f"MPU{self.owner.get_id()}.WLEngine: Reduced to new temp_prop = {vtemp}.")
        work_list_item.set_temp_prop(vtemp)
        print(f"MPU{self.owner.get_id()}.WLEngine: Setting valid for WorkListItem.")
        work_list_item.validate()
        self.owner.write_work_list_item(vid, work_list_item)
        print(f"MPU{self.owner.get_id()}.WLEngine: Sending candidate to Apply.")
        self.owner.recv_candidate(vid)
