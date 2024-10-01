import networkx as nx

def buggy_1(G, nodes=None):
    cliques = list(nx.find_cliques(G))
    for i in range(len(cliques)):
        if len(cliques[i]) > 1:
            cliques[i].append(cliques[i][0])  # Duplicate a node, increasing the clique size.
    return cliques

def buggy_2(G, nodes=None):
    cliques = list(nx.find_cliques(G))
    for i in range(len(cliques)):
        if len(cliques[i]) > 2:
            cliques[i] = cliques[i][:-1]  # Remove a node, reducing the size.
    return cliques

def buggy_3(G, nodes=None):
    cliques = list(nx.find_cliques(G))
    for i in range(len(cliques)):
        if len(cliques[i]) > 2:
            cliques[i][0] = cliques[i][1]  # Replace a node with another one, making it invalid.
    return cliques

def buggy_4(G, nodes=None):
    cliques = list(nx.find_cliques(G))
    if len(cliques) > 0:
        cliques[0].append(9999)  # Add a non-existent node to a clique, making it larger.
    return cliques

def buggy_5(G, nodes=None):
    cliques = list(nx.find_cliques(G))
    for i in range(len(cliques)):
        cliques[i] = sorted(cliques[i], reverse=True)  # Sort nodes in descending order, altering the correct order.
    return cliques