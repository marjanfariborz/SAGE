import re
import json

from json.encoder import JSONEncoder

class Vertex():
    def __init__(self, vid, dst = None, value = float('inf')):
        self.id = vid
        self.neighbors = []
        self.value = value
        self.tempValue = value
        if dst is not None:
            self.neighbors.append(dst)

    def add_neighbor(self, dst):
        self.neighbors.append(dst)

    def write_value(self, value):
        self.value.append(value)

    def read_value(self):
        return self.value

    def get_neighbors(self):
        return self.neighbors

    def __str__(self):
        ret = f"id={self.id}, neighbours={self.neighbors}\n"
        return ret

    def __repr__(self):
        return str(self)

    def get_neighbors(self):
        return self.neighbors

    def __str__(self):
        ret = f"id={self.id}, neighbours={self.neighbors}\n"
        return ret

    def __repr__(self):
        return str(self)

class VertexEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Channel():
    def __init__(self, cid, vertices = None):
        self.id = cid

        self.vertices = []
        if vertices is not None:
            self.vertices = vertices

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def __str__(self):
        ret = ""
        for vertex in self.vertices:
            ret += str(vertex)
        return ret

    def __repr__(self):
        return str(self)

def read_graph(file_name):
    vertices = {}

    with open(file_name, "r") as graph:
        for line in graph.readlines():
            if not line.startswith("#"):
                src, dst = line.split()
                src = int(src)
                dst = int(dst)
                if src in vertices.keys():
                    vertices[src].add_neighbor(dst)
                else:
                    vertices[src] = Vertex(src, dst)

    vertex_list = []
    for _, value in vertices.items():
        vertex_list.append(value)

    return vertex_list

def graph_to_json(file_name):
    vertex_list = read_graph(file_name)
    json_name = re.sub(r"\..*", ".json", file_name)
    with open(json_name, "w") as json_file:
        json.dump(vertex_list, json_file, indent = 2, cls = VertexEncoder)

def create_channels(num_channels, vertex_list):
    channels = [Channel(i) for i in range(num_channels)]
    for vertex in vertex_list:
        channels[(vertex.id % num_channels)].add_vertex(vertex)
    return channels

if __name__ == "__main__":
    # graph_to_json("roadNet-CA.txt")
    vertex_list = read_graph("roadNet-CA.txt")
    channels = create_channels(2, vertex_list)
    print(channels[1])
