from os import stat
from anything import Anything
class Solution():
    def __init__(self, vid, prop):
        self.vid = vid
        self.prop = prop

    def __str__(self):
        return f"[vid={self.vid}, prop={self.prop}]"

    def __repr__(self):
        return str(self)

class MemoryDevice(Anything):
    def __init__(self, owner, mid, debug_print=False):
        super().__init__(owner, mid, debug_print)
        self.set_name()
        self.vertices = []

    def add_vertex(self, vertex):
        self.vertices = self.vertices + [vertex]

    def read_edge_list(self, vid):
        self.print_debug(f"Fetching the EdgeList for vid {vid}")
        for vertex in self.vertices:
            if vertex.get_id() == vid:
                edges = vertex.get_edges()
                self.print_debug(f"Fetched the Edgelist for vid {vid}.\nEdgeList: {edges}")
                return edges
        raise Exception(f"I don't have a vertex with id {vid}")

    # TODO: Ask Marjan about this
    def append_work_list_item(self, wl_item):
        self.work_list.append(wl_item)

    def read_work_list_item(self, vid):
        self.print_debug(f"Fetching the WorkListItem for vid {vid}.")
        for vertex in self.vertices:
            if vertex.get_id() == vid:
                return vertex.get_work_list_item()

    def write_work_list_item(self, vid, wl_item):
        self.print_debug(f"Writing the WorkListItem for vid {vid}.\nWorkListItem: {wl_item}")
        for i in range(len(self.vertices)):
            if self.vertices[i].get_id() == vid:
                self.vertices[i].set_work_list_item(wl_item)
                return
        raise Exception(f"I don't have a vertex with id {vid}")

    def has_vertex(self, vid):
        for vertex in self.vertices:
            if vertex.get_id() == vid:
                return True
        return False

    def get_solutions(self):
        solutions = []
        for vertex in self.vertices:
            solutions.append(Solution(vertex.get_id(), vertex.get_work_list_item().get_prop()))
        return solutions

    def get_vertex_stats(self):
        stats = []
        for vertex in self.vertices:
            stats.append(vertex.get_stats())
        return stats

    def __str__(self):
        return f"MemoryDevice[vertices={self.vertices}]"

    def __repr__(self):
        return str(self)
