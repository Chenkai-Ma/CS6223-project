import networkx as nx

def buggy_1(G, nodes=None):
    return [c for c in nx.find_cliques(G)] * 2  # Repeat the cliques twice

def buggy_2(G, nodes=None):
    return list(nx.find_cliques(G)) + [[0, 1]]  # Append a known clique to all results

def buggy_3(G, nodes=None):
    cliques = list(nx.find_cliques(G))
    return cliques + cliques[-1:]  # Append the last clique to the result

def buggy_4(G, nodes=None):
    return list(nx.find_cliques(G)) + [[2, 3]] * 10  # Append a known clique multiple times

def buggy_5(G, nodes=None):
    cliques = list(nx.find_cliques(G))
    # append the same clique to the result twice
    return cliques + cliques[:1] + cliques[:1]