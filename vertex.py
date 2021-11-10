from math import inf
from json.encoder import JSONEncoder


class Edge:
    def __init__(self, neighbor, weight):
        self.neighbor = neighbor
        self.weight = weight

    def get_neighbor(self):
        return self.neighbor

    def get_weight(self):
        return self.weight

    def __str__(self):
        return f"Edge[neighbor={self.neighbor}, weight={self.weight}]"

    def __repr__(self):
        return str(self)


class WorkListItem:
    def __init__(self, temp_prop, prop, valid):
        self.temp_prop = temp_prop
        self.prop = prop
        self.valid = valid

    def get_temp_prop(self):
        return self.temp_prop

    def get_prop(self):
        return self.prop

    def set_temp_prop(self, temp_prop):
        self.temp_prop = temp_prop

    def set_prop(self, prop):
        self.prop = prop

    def is_valid(self):
        return self.valid

    def validate(self):
        self.valid = True

    def invalidate(self):
        self.valid = False

    def __str__(self):
        ret = f"WorkListItem[temp_prop={self.temp_prop}, prop={self.prop}, valid={self.valid}]"
        return ret

    def __repr__(self):
        return str(self)

class VertexStats():
    def __init__(self):
        self.num_wl_item_reads = 0
        self.num_wl_item_writes = 0
        self.num_edge_list_reads = 0

    def get_dict(self):
        return self.__dict__

class Vertex:
    def __init__(self, vid):
        self.id = vid
        self.address = None
        self.degree = 0
        self.work_list_item = WorkListItem(
            temp_prop=inf, prop=inf, valid=False
        )
        self.edges = []
        self.stats = VertexStats()

    def get_id(self):
        return self.id

    # NOTE: Probably not needed
    def new_id(self, vid):
        self.id = vid

    def get_work_list_item(self):
        self.stats.num_wl_item_reads += 1
        return self.work_list_item

    def set_work_list_item(self, item):
        self.stats.num_wl_item_writes += 1
        self.work_list_item = item

    def add_edge(self, edge):
        self.edges.append(edge)

    # NOTE: Probably not needed
    def update_edge(self, new_edge, index):
        self.edges[index] = new_edge

    def get_edges(self):
        self.stats.num_edge_list_reads += 1
        return self.edges

    def set_edges(self, edges):
        self.edges = edges

    def get_degree(self):
        return self.degree

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def increase_degree(self):
        self.degree = self.degree + 1

    def get_stats(self):
        stats = self.stats.get_dict()
        stats["vid"] = self.id
        stats["degree"] = self.degree
        return stats

    def __str__(self):
        return f"Vertex[id={self.id}, degree={self.degree}, work_list={self.work_list_item}, edges={self.edges}]"

    def __repr__(self):
        return str(self)


class VertexEncoder(JSONEncoder):
    def default(self, vertex):
        ret = dict()
        ret["id"] = vertex.get_id()
        ret["address"] = vertex.get_address()
        ret["degree"] = vertex.get_degree()
        ret["work_list_item"] = vertex.get_work_list_item().__dict__
        ret["edges"] = []
        for edge in vertex.get_edges():
            ret["edges"].append(edge.__dict__)
        return ret

# TODO: Implement JSONDecoder
