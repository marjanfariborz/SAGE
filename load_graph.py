import re
import json

from mpu import MPU
from vertex import Edge, Vertex, VertexEncoder


def read_graph(file_name):
    vertices = {}
    with open(file_name, "r") as graph:
        for line in graph.readlines():
            if not line.startswith("#"):
                src, dst = line.split()
                src = int(src)
                dst = int(dst)
                if src in vertices.keys():
                    edge = Edge(dst, 0)
                    vertices[src].add_edge(edge)
                    vertices[src].increase_degree()
                else:
                    vertices[src] = Vertex(src)
                    edge = Edge(dst, 0)
                    vertices[src].add_edge(edge)
                    vertices[src].increase_degree()

    return vertices

def calculate_addresses(graph):
    consume = 0
    for vid in graph.keys():
        degree = graph[vid].get_degree()
        graph[vid].set_address(consume)
        consume = consume + 16 + (degree * 12)
        consume = consume + (64 - (consume % 64))

    return graph

def update_edges(graph):
    for vid in graph.keys():
        edges = graph[vid].get_edges()
        new_edges = []
        for edge in edges:
            dst_vid = edge.get_neighbor()
            weight = edge.get_weight()
            dst_addr = graph[dst_vid].get_address()
            new_edge = Edge(dst_addr, weight)
            new_edges.append(new_edges)
        graph[vid].set_edges(new_edges)

    return graph

def dict_to_list(graph):
    out_list = []
    for _, vertex in graph.items():
        out_list.append(vertex)
    return out_list

def initialize_mpu(vertices):
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

def graph_to_json(graph, out_name):
    with open(out_name, "w") as json_file:
        json.dump(graph, json_file, indent = 2, cls = VertexEncoder)

def create_channels(num_channels, vertex_list):
    channels = [Channel(i) for i in range(num_channels)]
    for vertex in vertex_list:
        channels[(vertex.id % num_channels)].add_vertex(vertex)
    return channels



if __name__ == "__main__":
    # graph_to_json("roadNet-CA.txt")
    # mpu_num = 2
    # vertex_list = read_graph("roadNet-CA.txt", mpu_num)
    # print(vertex_list[0])
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
    graph_dict = read_graph("roadNet-CA.txt")
    graph_dict = calculate_addresses(graph_dict)
    graph_list = dict_to_list(graph_dict)
    # print(graph_list)
    graph_to_json(graph_list, "roadNet-CA.json")