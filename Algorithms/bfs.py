from check import correctness
from math import inf

def read_graph(file_name):
    vertices = {}
    with open(file_name, "r") as graph:
        for line in graph.readlines():
            if not line.startswith("#"):
                src, dst = line.split()
                src = str(src)
                dst = str(dst)
                if src in vertices.keys():
                    vertices[src].append(dst)
                else:
                    vertices[src] = [dst]
                if dst not in vertices:
                    vertices[dst] = []

    return vertices

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def init_prop(graph):
    prop = {}
    for i in graph.keys():
        prop[i] = float(inf)
    return prop

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    prop = init_prop(graph)
    prop[node] = 0

    while queue:
        s = queue.pop(0)

        for neighbour in graph[s]:
        #   if neighbour not in visited:
            # visited.append(neighbour)
            temp_prop = int(prop[s]) + 1
            # print(temp_prop)
            if neighbour not in prop:
                prop[neighbour] = temp_prop
                queue.append(neighbour)
            elif temp_prop < prop[neighbour]:
                prop[neighbour] = temp_prop
                queue.append(neighbour)
    return prop

# Driver Code
oracle = bfs(visited, read_graph("twitter_combined.txt"), str(214328887))
# print(oracle)
correctness(oracle, 'sage_solution_twitter_combined_bfs.txt')
