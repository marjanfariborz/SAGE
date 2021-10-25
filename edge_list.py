from json.encoder import JSONEncoder

class EdgeList():
    def __init__(self, vid, dst = None, value = float('inf')):
        self.id = vid
        self.neighbors = []
        self.value = value
        self.tempValue = value
        if dst is not None:
            self.neighbors.append(dst)

    def get_id(self):
        return self.id

    def add_neighbor(self, dst):
        self.neighbors.append(dst)

    def write_value(self, value):
        self.value.append(value)

    def read_value(self):
        return self.value

    def get_neighbors(self):
        return self.neighbors

    def __str__(self):
        ret = f"EdgeList[id={self.id}, neighbours={self.neighbors}]"
        return ret

    def __repr__(self):
        return str(self)

    def get_neighbors(self):
        return self.neighbors

class EdgeListEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
