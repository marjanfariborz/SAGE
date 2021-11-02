from json.encoder import JSONEncoder

class Edge():
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

class WorkListItem():
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
        ret = f"WorkListItem[temp_prop={self.temp_prop}, prop={self.prop}, valid={self.valid}]"
        return ret

    def __repr__(self):
        return str(self)

class Vertex():
    def __init__(self, vid):
        self.id = vid
        self.edges = []
        self.degree = 0
        self.address = None
        self.work_list_item = None

    def get_id(self):
        return self.id

    def new_id(self, id):
        self.id = id

    def add_edge(self, edge):
        self.edges.append(edge)

    def update_edge(self, new_edge, index):
        self.edges[index] = new_edge

    def get_edges(self):
        return self.edges

    def get_degree(self):
        return self.degree

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def increase_degree(self):
        self.degree = int(self.get_degree()) + 1


    def __str__(self):
        ret = f"EdgeList[id={self.id}, neighbours={self.edges}, degree={self.degree}]"
        return ret

    def __repr__(self):
        return str(self)


class EdgeListEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
