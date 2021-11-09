import argparse

from mpu import MPU, DebugFlags
from update import Update
from network import Network
from load_graph import read_graph, dict_to_list


def reduce_function(value, temp_prop):
    return min(value, temp_prop)


def propagate_function(value, weight):
    return value + 1


parser = argparse.ArgumentParser()

parser.add_argument(
    "graph",
    type=str,
    help="Name of the graph file to process",
)
parser.add_argument("--outdir", type=str, help="Path to save the output")
parser.add_argument(
    "--debug_wl_engine",
    action="store_true",
    help="Define this argument to get debug prints for WLEngines",
)
parser.add_argument(
    "--debug_apply",
    action="store_true",
    help="Define this argument to get debug prints for Applies",
)
parser.add_argument(
    "--debug_push",
    action="store_true",
    help="Define this argument to get debug prints for Pushes",
)
parser.add_argument(
    "--debug_mem_dev",
    action="store_true",
    help="Define this argument to get debug prints for MemoryDevices",
)

def parse_arguments(parser):
    args = parser.parse_args()
    graph = args.graph
    outdir = args.outdir
    if outdir is None:
        outdir = "."
    debug_flags = {}
    debug_flags["wl_engine_debug"] = args.debug_wl_engine
    debug_flags["apply_debug"] = args.debug_apply
    debug_flags["push_debug"] = args.debug_push
    debug_flags["mem_dev_debug"] = args.debug_mem_dev
    return graph, outdir, debug_flags

if __name__ == "__main__":
    graph, outdir, debug_flags = parse_arguments(parser)
    graph = read_graph(graph)
    vertex_list = dict_to_list(graph)

    num_mpus = 2
    network = Network()
    mpus = [
        MPU(
            mid=i,
            network=network,
            propagate=propagate_function,
            reduce=reduce_function,
            debug_flags=debug_flags,
        )
        for i in range(num_mpus)
    ]
    network.set_mpus(mpus)
    for vertex in vertex_list:
        mpus[vertex.get_id() % num_mpus].add_vertex(vertex)

    initial_update = Update(0, 0)

    network.send_initial_update(initial_update)
