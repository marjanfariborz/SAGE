import re
import json

from json.encoder import JSONEncoder

class Vertex():
    def __init__(self, vid, dst = None, value = float('inf')):
        self.id = vid
        self.neighbors = []
        self.value = value
        if dst is not None:
            self.neighbors.append(dst)

    def add_neighbor(self, dst):
        self.neighbors.append(dst)

    def write_value(self, value):
        self.value.append(value)

    def read_value(self, value):
        return value

class VertexEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def read_graph(file_name):
    vertices = {}

    with open(file_name, "r") as graph:
        for line in graph.readlines():
            if not line.startswith("#"):
                src, dst = line.split()
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

if __name__ == "__main__":
    graph_to_json("roadNet-CA.txt")
