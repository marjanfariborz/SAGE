from math import inf
import numpy as np
from scipy.sparse import csr_matrix
import multiprocessing

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
    print(f"Max number of vertecies:{num_v} ")
    rows, cols, vals = zip(*Graph)
    a = csr_matrix((vals, (rows, cols)))
    prop = [inf]*(num_v+1)
    return a, prop, num_v+1

Graph, vertex_prop, num_v = GraphStructure('USA-road-d.NY.gr')
Graph_arr = Graph.toarray()
print(Graph_arr)
keys = [i for i in range(num_v)]
event_queue = {key: None for key in keys}
event_queue[0] = 0
itr = int(0)
n = 0
while(1):
    if (all(value == None for value in event_queue.values())):
        break
    n += 1
    for key, value in event_queue.items():
        if value != None:
            temp = vertex_prop[key]
            vertex_prop[key] = min(vertex_prop[key], value)

            if temp != 0:
                itr += 1
                # print(itr)
                row = Graph_arr[key]
                for i,val in enumerate(row):
                    if val != 0:
                        event_queue[i]=0
                event_queue[key] = None
            else:
                event_queue[key] = None

for i, k in enumerate(vertex_prop):
    if k == inf:
        print(i)
# print(vertex_prop)