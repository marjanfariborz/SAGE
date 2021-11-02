import re
from vertex import Vertex

def read_graph(file_name):
    vertices = {}
    count = 0
    pf_sum = []
    with open(file_name, "r") as graph:
        for line in graph.readlines():
            if not line.startswith("#"):
                src, dst = line.split()
                src = int(src)
                dst = int(dst)
                if src in vertices.keys():
                    vertices[src].add_edge(dst)
                    vertices[src].increase_degree()
                else:
                    count = count + 1
                    vertices[src] = Vertex(src)
                    vertices[src].add_edge(dst)
                    vertices[src].increase_degree()
    id_degree = {}
    degree = []
    consume = 0
    for _, vertex in vertices.items():
        id = vertex.get_id()
        degree = vertex.get_degree()
        vertex.set_address(consume)
        consume = consume + degree * 28

    vertex_list = []
    for _, vertex in vertices.items():
        neighbors = vertex.get_edges()
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            new_id = vertices[neighbor].get_address()
            vertex.update_edge(new_id, i)
        # print(vertex.get_id(), vertex.get_edges())

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
    # channels = create_channels(2, vertex_list)
    print(vertex_list)
