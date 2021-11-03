from wl_engine import WLEngine
from memory_device import MemoryDevice
from reduce_apply import Apply
from push import Push

class MPU():
    def __init__(self, mid, network, propagate, reduce):
        self.id = mid
        self.wl_engine = WLEngine(self, reduce)
        self.reduce_apply = Apply(self, reduce)
        self.push = Push(self, propagate)
        self.mem_dev = MemoryDevice(self)
        self.network = network

    def read_work_list_item(self, vid):
        return self.mem_dev.read_work_list_item(vid)

    def append_work_list_item(self, item):
        self.mem_dev.append_work_list_item(item)

    def write_work_list_item(self, item):
        self.mem_dev.write_work_list_item(item)

    def write_edge_list(self, edge_list):
        self.mem_dev.write_edge_list(edge_list)

    def read_edge_list(self, vid):
        self.mem_dev.read_edge_list(vid)

    def recv_candidate(self, vid):
        self.reduce_apply.recv_candidate(vid)

    def recv_work(self, edges, new_prop):
        self.push.recv_work(edges, new_prop)

    def recv_update(self, updates):
        self.network.recv_update(updates)

    def get_id(self):
        return self.id

