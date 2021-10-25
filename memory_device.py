
class MemoryDevice():
    def __init__(self, owner, edge_lists = None, work_list = None):
        self.owner = owner
        self.edge_lists = []
        if edge_lists is not None:
            self.edge_lists = edge_lists

        self.work_list = []
        if work_list is not None:
            self.work_list = work_list

    def write_edge_list(self, edge_list):
        self.edge_lists.append(edge_list)

    def read_edge_list(self, vid):
        for edge_list in self.edge_lists:
            if edge_list.get_id() == vid:
                return edge_list
        raise Exception(f"Could not find the edge list with vid: {vid}")

    def write_work_list_item(self, wl_item):
        for i in range(len(self.work_list)):
            if  wl_item.get_id() == self.work_list[i].get_id():
                self.work_list[i] = wl_item
                return
        self.work_list.append(wl_item)

    def read_work_list_item(self, vid):
        for item in self.work_list:
            if vid == item.get_id():
                return item

    def __str__(self):
        return f"channel[edge_lists={str(self.vertices)}, work_list={str(self.work_list)}]"

    def __repr__(self):
        return str(self)
