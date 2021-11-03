import re

from vertex import Edge, Vertex

def read_graph(file_name):
    vertices = {}

    with open(file_name, "r") as graph:
        for line in graph.readlines():
            if not line.startswith("#"):
                src, dst = line.split()
                src = int(src)
                dst = int(dst)
                if src in vertices.keys():
                    # TODO: read weight from graph
                    edge = Edge(dst, 0)
                    vertices[src].add_edge(edge)

                else:
                    vertices[src] = Vertex(src)

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
