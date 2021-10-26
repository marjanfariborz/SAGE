from wl_engine import WLEngine
from memory_device import MemoryDevice

class MPU():
    def __init__(self, mid, operation):
        self.id = mid
        self.wl_engine = WLEngine(self, operation)
        self.mem_dev = MemoryDevice(self)

    def read_work_list_item(self, vid):
        return self.mem_dev.read_work_list_item(vid)

    def write_work_list_item(self, item):
        self.mem_dev.write_work_list_item(item)

    def write_edge_list(self, edge_list):
        self.mem_dev.write_edge_list(edge_list)

    def read_edge_list(self, vid):
        self.mem_dev.read_work_list_item(vid)

    def get_id(self):
        return self.id

