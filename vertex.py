from json.encoder import JSONEncoder

class Edge():
    def __init__(self, neighbor, weight):
        self.neighbor = neighbor
        self.weight = weight

class WorkListItem():
    def __init__(self, vid, temp_prop, prop, valid):
        self.vid = vid
        self.temp_prop = temp_prop
        self.prop = prop
        self.valid = valid

    def get_temp_prop(self):
        return self.temp_prop

    def set_temp_prop(self, temp_prop):
        self.temp_prop = temp_prop

    def get_prop(self):
        return self.prop

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
        self.work_list_item = None

    def get_id(self):
        return self.id

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_edges(self):
        return self.edges

    def __str__(self):
        ret = f"EdgeList[id={self.id}, neighbours={self.edges}]"
        return ret

    def __repr__(self):
        return str(self)


class EdgeListEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
