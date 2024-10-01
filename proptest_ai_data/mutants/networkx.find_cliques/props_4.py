import networkx as nx

# Buggy Version 1: Remove an arbitrary node from each clique. This will break the completeness as at least one edge will be missing.
def buggy_1(G):
    cliques = nx.find_cliques(G)
    return [clique[:-1] for clique in cliques]

# Buggy Version 2: Add an arbitrary node to each clique. This will break the completeness as the new node is not adjacent with all the other nodes of the clique
def buggy_2(G):
    cliques = nx.find_cliques(G)
    return [clique + [list(G.nodes)[-1]] for clique in cliques]

# Buggy Version 3: Merge two arbitrary cliques. This will break the completeness as there may be no edge between some nodes of different cliques
def buggy_3(G):
    cliques = list(nx.find_cliques(G))
    if len(cliques) > 1:
        return [cliques[0] + cliques[1]] + cliques[2:]
    else:
        return cliques

# Buggy Version 4: Create a new clique with arbitrary nodes. This will break the completeness as there may be no edge between some nodes of the new clique
def buggy_4(G):
    cliques = nx.find_cliques(G)
    if len(G.nodes) > 2:
        return cliques + [[list(G.nodes)[0], list(G.nodes)[1]]]
    else:
        return cliques

# Buggy Version 5: Replace a node in a clique with another arbitrary node. This will break the completeness as the new node is not adjacent with all the other nodes of the clique
def buggy_5(G):
    cliques = nx.find_cliques(G)
    return [[list(G.nodes)[-1] if n == list(G.nodes)[0] else n for n in clique] for clique in cliques]