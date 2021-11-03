
class MemoryDevice():
    def __init__(self, owner):
        self.owner = owner
        self.vertices = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def read_edge_list(self, vid):
        for vertex in self.vertices():
            if vertex.get_id() == vid:
                return vertex.get_edges()
        raise Exception(f"I don't have a vertex with id {vid}")

    # TODO: Ask Marjan about this
    def append_work_list_item(self, wl_item):
        self.work_list.append(wl_item)

    def read_work_list_item(self, vid):
        for vertex in self.vertices():
            if vertex.get_id() == vid:
                return vertex.get_work_list_item()

    def write_work_list_item(self, vid, wl_item):
        for i in range(len(self.vertices())):
            if self.vertices[i].get_id() == vid:
                self.vertices[i].set_work_list_item(wl_item)
        raise Exception(f"I don't have a vertex with id {vid}")

    def has_vertex(self, vid):
        for vertex in self.vertices:
            if vertex.get_id() == vid:
                return True
        return False

    def __str__(self):
        return f"MemoryDevice[vertices={self.vertices}]"

    def __repr__(self):
        return str(self)
