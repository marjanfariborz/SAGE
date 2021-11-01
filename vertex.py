from json.encoder import JSONEncoder


class Edge:
    def __init__(self, vid, neighbor, weight):
        self.vid = vid
        self.neighbor = neighbor
        self.weight = weight

    def get_vid(self):
        return self.vid

    def get_neighbor(self):
        return self.neighbor

    def get_weight(self):
        return self.weight

    def __str__(self):
        return f"Edge[vid={self.vid}, neighbor={self.neighbor}, weight={self.weight}]"

    def __repr__(self):
        return str(self)

class WorkListItem:
    def __init__(self, vid, temp_prop, prop, valid):
        self.vid = vid
        self.temp_prop = temp_prop
        self.prop = prop
        self.valid = valid

    def get_vid(self):
        return self.vid

    def get_temp_prop(self):
        return self.temp_prop

    def get_prop(self):
        return self.prop

    def set_prop(self, temp_prop):
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
        ret = f"WorkListItem[vid={self.vid}, temp_prop={self.temp_prop}, prop={self.prop}, valid={self.valid}]"
        return ret

    def __repr__(self):
        return str(self)


class Vertex:
    def __init__(self, vid):
        self.id = vid
        self.address = None
        self.out_degree = 0
        self.work_list_item = WorkListItem(
            vid=self.id, temp_prop=-1, prop=-1, valid=False
        )
        self.edges = []

    def get_id(self):
        return self.id

    def new_id(self, vid):
        self.id = vid

    def get_work_list_item(self):
        return self.work_list_item

    def set_work_list_item(self, item):
        self.work_list_item = item

    def add_edge(self, edge):
        self.edges.append(edge)

    def update_edge(self, new_edge, index):
        self.edges[index] = new_edge

    def get_edges(self):
        return self.edges

    def get_out_degree(self):
        return self.out_degree

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def increase_out_degree(self):
        self.out_degree = self.out_degree + 1

    def __str__(self):
        return f"Vertex[id={self.id}, degree={self.degree}, work_list={str(self.work_list_item)}, edges={str(self.edges)}]"

    def __repr__(self):
        return str(self)

class VertexEncoder(JSONEncoder):
    def default(self, vertex):
        ret = dict()
        ret["id"] = vertex.get_id()
        ret["work_list_item"] = vertex.get_work_list_item().__dict__
        ret["edges"] = []
        for edge in vertex.get_edges():
            ret["edges"].append(edge.__dict__)
        return ret
