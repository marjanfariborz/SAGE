from math import inf
import numpy as np
from scipy.sparse import csr_matrix
import multiprocessing
import numpy as np

def GraphStructure(graphFile):
    Graph = []
    EdgeList = []
    f = open(graphFile, "r")
    for line in f:
        if line.startswith('a'):
            line = line.strip()
            p = line.split(' ')
            n = [ int(x)-1 for x in p[1:]]
            Graph.append(n)
            EdgeList.append(n[0:1])
    gr = np.array(Graph, dtype=int)
    el = np.array(EdgeList, dtype=int)
    num_v = np.amax(el)
    print(f"Max number of vertecies:{num_v}")
    rows, cols, vals = zip(*Graph)
    a = csr_matrix((vals, (rows, cols)))
    prop = [inf]*(num_v+1)
    return a, prop, num_v+1

def degree_count(graph):
    Graph, vertex_prop, num_v = GraphStructure(graph)
    file = open('degree_count.csv', 'w')
    Graph_arr = Graph.toarray()
    degree_list = []
    for row in Graph_arr:
        degree = 0
        for index in row:
            if index != 0:
                degree += 1
        degree_list.append(degree)
        file.write(str(degree))
        file.write('\n')

def action(algorithm):
    if algorithm == 'BFS':
        return min, min
    elif algorithm == 'SSSP':
        return min, sum

def main(algorithm, graph):
    Graph, vertex_prop, num_v = GraphStructure(graph)
    Graph_arr = Graph.toarray()
    print(Graph_arr)
    keys = [i for i in range(num_v)]
    event_queue = {key: None for key in keys}
    event_queue[0] = 0
    itr = int(0)
    n = 0
    reduce, propagate = action(algorithm)
    while(1):
        if (all(value == None for value in event_queue.values())):
            break
        n += 1
        for vertex, paylaod in event_queue.items():
            if paylaod != None:
                temp = vertex_prop[vertex]
                vertex_prop[vertex] = reduce(vertex_prop[vertex], paylaod)
                if 0 < abs(temp - vertex_prop[vertex]):
                    itr += 1
                    row = Graph_arr[vertex]
                    for i,val in enumerate(row):
                        if val != 0:
                            if event_queue[i] != None:
                                event_queue[i]= reduce(propagate([0, val]), event_queue[i])
                            else:
                                event_queue[i]= propagate([0, val])
                    event_queue[vertex] = None
                else:
                    event_queue[vertex] = None

main('BFS', 'USA-road-d.NY.gr')

