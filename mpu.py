from push import Push
from apply import Apply
from anything import Anything
from argparse import Namespace
from wl_engine import WLEngine
from memory_device import MemoryDevice


class DebugFlags():
    def __init__(self):
        self.wl_engine_debug = False
        self.apply_debug = False
        self.push_debug = False
        self.mem_dev_debug = False

    def set_flags(self, flags):
        if isinstance(flags, dict):
            if "wl_engine_debug" in flags:
                self.wl_engine_debug = flags["wl_engine_debug"]
            if "apply_debug" in flags:
                self.apply_debug = flags["apply_debug"]
            if "push_debug" in flags:
                self.push_debug = flags["push_debug"]
            if "mem_dev_debug" in flags:
                self.mem_dev_debug = flags["mem_dev_debug"]
        elif isinstance(flags, Namespace):
            if flags.wl_engine_debug is not None:
                self.wl_engine_debug = flags.wl_engine_debug
            if flags.apply_debug is not None:
                self.apply_debug = flags.apply_debug
            if flags.push_debug is not None:
                self.push_debug = flags.push_debug
            if flags.mem_dev_debug is not None:
                self.mem_dev_debug = flags.mem_dev_debug
        elif flags is None:
            pass
        else:
            raise Exception("DebugFlags.set_flags only accepts a dictionary, an argparse.Namespace, or a None")

class MPU(Anything):
    def __init__(self, mid, network, propagate, reduce, debug_flags=None):
        super().__init__(network, mid, debug_print=False)
        self.set_name()
        self.debug_flags = DebugFlags()
        self.debug_flags.set_flags(debug_flags)
        self.wl_engine = WLEngine(self, 0, reduce, debug_print=self.debug_flags.wl_engine_debug)
        self.apply = Apply(self, 0, reduce, debug_print=self.debug_flags.apply_debug)
        self.push = Push(self, 0, propagate, debug_print=self.debug_flags.push_debug)
        self.mem_dev = MemoryDevice(self, 0, debug_print=self.debug_flags.mem_dev_debug)
        self.network = network

    def get_name(self):
        return self.name

    def read_work_list_item(self, vid):
        return self.mem_dev.read_work_list_item(vid)

    def append_work_list_item(self, item):
        self.mem_dev.append_work_list_item(item)

    def write_work_list_item(self, vid, item):
        self.mem_dev.write_work_list_item(vid, item)

    def write_edge_list(self, edge_list):
        self.mem_dev.write_edge_list(edge_list)

    def read_edge_list(self, vid):
        return self.mem_dev.read_edge_list(vid)

    def recv_candidate(self, vid):
        self.apply.recv_candidate(vid)

    def recv_work(self, edges, new_prop):
        self.push.recv_work(edges, new_prop)

    def recv_updates(self, updates):
        self.network.recv_updates(updates)

    def recv_update(self, update):
        self.wl_engine.recv_update(update)

    def get_id(self):
        return self.id

    def add_vertex(self, vertex):
        self.mem_dev.add_vertex(vertex)

    def has_vertex(self, vid):
        return self.mem_dev.has_vertex(vid)

    def get_solutions(self):
        return self.mem_dev.get_solutions()

    def __str__(self):
        return f"MPU[id={self.id}, memory={self.mem_dev}]"

    def __repr__(self):
        return str(self)
