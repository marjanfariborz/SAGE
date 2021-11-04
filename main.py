from mpu import MPU
from update import Update
from network import Network
from load_graph import read_graph, dict_to_list


def reduce_function(value, temp_prop):
    return min(value, temp_prop)


def propagate_function(value, weight):
    return value + 1


if __name__ == "__main__":
    graph = read_graph("test-graph.txt")
    vertex_list = dict_to_list(graph)

    num_mpus = 2
    network = Network()
    mpus = [
        MPU(
            mid=i,
            network=network,
            propagate=propagate_function,
            reduce=reduce_function,
        )
        for i in range(num_mpus)
    ]
    network.set_mpus(mpus)
    for vertex in vertex_list:
        mpus[vertex.get_id() % num_mpus].add_vertex(vertex)

    print(mpus)
    print()

    initial_update = Update(0, 0)

    network.send_initial_update(initial_update)
