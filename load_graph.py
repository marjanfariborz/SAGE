import re
from math import inf
from vertex import Vertex, WorkListItem, Edge
from mpu import MPU

def read_graph(file_name, mpu_num):
    vertices = {}
    count = 0
    with open(file_name, "r") as graph:
        for line in graph.readlines():
            if not line.startswith("#"):
                src, dst = line.split()
                src = int(src)
                dst = int(dst)
                if src in vertices.keys():
                    vertices[src].add_edge(dst)
                    vertices[src].increase_out_degree()
                else:
                    count = count + 1
                    vertices[src] = Vertex(src)
                    vertices[src].add_edge(dst)
                    vertices[src].increase_out_degree()
    degree = []
    consume = 0
    for _, vertex in vertices.items():
        id = vertex.get_id()
        degree = vertex.get_out_degree()
        vertex.set_address(consume)
        consume = consume + degree * 28

    vertex_list = []
    mpu = [MPU(i, sum, min) for i in range(mpu_num)]
    for _, vertex in vertices.items():
        neighbors = vertex.get_edges()
        id = vertex.get_address()
        mpu_n = id % mpu_num
        wl = WorkListItem(id, float(inf), float(inf), 0)
        edge_list = []
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            new_id = vertices[neighbor].get_address()
            vertex.update_edge(new_id, i)
            edge_list.append(Edge(id, new_id, 1))
        mpu[mpu_n].write_edge_list(edge_list)
        mpu[mpu_n].append_work_list_item(wl)
    # print(mpu[0].read_work_list_item(0))
    # print(mpu[0].read_edge_list(0))

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
    mpu_num = 2
    vertex_list = read_graph("roadNet-CA.txt", mpu_num)
    print(vertex_list[0])
    # channels = create_channels(2, vertex_list)

    # mpu = [MPU(i, sum, min) for i in range(mpu_num)]
    # for _, vertex in vertex_list:
    #     id = vertex.get_address()
    #     mpu_n = id % mpu_num
    #     wl = WorkListItem(id, int(inf), int(inf), 0)
    #     neighbors = vertex.get_edges
    #     edge_list = []
    #     for neighbor in neighbors:
    #         edge_list.append(Edge(id, neighbor, 1))
    #     mpu[mpu_n].write_edge_list(edge_list)
    #     mpu[mpu_n].write_work_list_item(wl)
