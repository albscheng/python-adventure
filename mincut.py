import random
import copy
import sys

def choose_random(graph):
    v1 = random.choice(list(graph.keys()))
    v2 = random.choice(list(graph[v1]))
    return v1, v2

def contract_edge(graph, u, v):
    # Add v's edges to u's edges
    graph[u].extend(graph[v])

    # Delete v
    # 1.  let all of v's neighbors know v is leaving
    for x in graph[v]:
        graph[x].remove(v)
        graph[x].append(u)
    del graph[v]
    #   Remove self-loops
    while u in graph[u]:
        graph[u].remove(u)

    return graph

def contract_graph(graph):
    # while graph has more than 2 vertices
    #   1. select a random edge
    #   2. collapse edge
    while len(graph) > 2:
        u, v = choose_random(graph)
        graph = contract_edge(graph, u, v)
    return graph

def karger(graph):
    length = []
    graph = contract_graph(graph)
    for key in graph.keys():
        length.append(len(graph[key]))
    return length[0]

if __name__ == '__main__':
    with open('kargerMinCut.txt', 'r') as data:
        adj_dict = {}
        for line in data:
            input_line = [int(s) for s in line.split()]
            adj_dict[input_line[0]] = input_line[1:]
    # adj_dict is now a dictionary with key = vertex
    # mapped to a list of edges

    debug_g = {1: [2, 3],
            2: [1, 3, 4],
            3: [1, 2, 4],
            4: [2, 3]}
  #  print contract_edge(debug_g, 1, 3)
    mincut = 100000

    for i in range(int(sys.argv[1])):
        temp_dict = copy.deepcopy(adj_dict)
        temp = karger(temp_dict)
        if temp < mincut:
            mincut = temp
            print mincut

