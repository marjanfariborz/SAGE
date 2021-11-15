import sys
import json
import types
import argparse

from mpu import MPU
from os import mkdir
from update import Update
from network import Network
from os.path import join, exists
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
parser.add_argument("--re", action="store_true")
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
parser.add_argument(
    "--debug_nw",
    action="store_true",
    help="Define this argument to get debug prints for MemoryDevices",
)

def parse_arguments(parser):
    args = parser.parse_args()
    graph = args.graph

    outdir = args.outdir
    if outdir is None:
        outdir = "sagesim_out"
    sim_flags = types.SimpleNamespace()
    sim_flags.re = args.re
    sim_flags.outdir = outdir

    mpu_debug_flags = types.SimpleNamespace()
    mpu_debug_flags.wl_engine_debug = args.debug_wl_engine
    mpu_debug_flags.apply_debug = args.debug_apply
    mpu_debug_flags.push_debug = args.debug_push
    mpu_debug_flags.mem_dev_debug = args.debug_mem_dev
    nw_debug_flag = args.debug_nw
    debug_flags = types.SimpleNamespace()
    debug_flags.mpu_debug_flags = mpu_debug_flags
    debug_flags.nw_debug_flag = nw_debug_flag

    return graph, sim_flags, debug_flags

if __name__ == "__main__":
    graph, sim_flags, debug_flags = parse_arguments(parser)
    graph = read_graph(graph)
    vertex_list = dict_to_list(graph)

    num_mpus = 2
    network = Network(debug_print=debug_flags.nw_debug_flag)
    mpus = [
        MPU(
            mid=i,
            network=network,
            propagate=propagate_function,
            reduce=reduce_function,
            debug_flags=debug_flags.mpu_debug_flags,
        )
        for i in range(num_mpus)
    ]
    network.set_mpus(mpus)
    initial_vertex_id = vertex_list[0].get_id()
    for vertex in vertex_list:
        mpus[vertex.get_id() % num_mpus].add_vertex(vertex)

    initial_update = Update(initial_vertex_id, 0)

    if not exists(sim_flags.outdir):
        mkdir(sim_flags.outdir)

    if sim_flags.re:
        sage_stdout = open(join(sim_flags.outdir, "sage_stdout"), "w")
        sage_stderr = open(join(sim_flags.outdir, "sage_stderr"), "w")
        sys.stdout = sage_stdout
        sys.stderr = sage_stderr

    network.send_initial_update(initial_update)

    solution = network.get_solution()
    with open(join(sim_flags.outdir, "solution.txt"), "w") as sol_file:
        sol_file.write(str(solution))

    vertex_stats = network.get_vertex_stats()
    with open(join(sim_flags.outdir, "vertex_stats.json"), "w") as vertex_file:
        json.dump(vertex_stats, vertex_file)

    mpu_stats = network.get_mpu_stats()
    with open(join(sim_flags.outdir, "mpu_stats.json"), "w") as mpu_file:
        json.dump(mpu_stats, mpu_file)

    if sim_flags.re:
        sage_stdout.close()
        sage_stderr.close()
