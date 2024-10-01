def buggy_1(G, nodes=None):
    cliques = list(nx.find_cliques(G))
    # Bug: Removing the first clique, can violate inclusiveness property if this clique was the one including 'nodes'
    if cliques:
        cliques.pop(0)
    return cliques

def buggy_2(G, nodes=None):
    cliques = list(nx.find_cliques(G))
    # Bug: Returning empty list will always violate the inclusiveness property
    return []

def buggy_3(G, nodes=None):
    cliques = list(nx.find_cliques(G))
    # Bug: Removing cliques that contain any of the given 'nodes'. This violates inclusiveness property as cliques including 'nodes' are eliminated
    if nodes:
        cliques = [clique for clique in cliques if not any(node in clique for node in nodes)]
    return cliques

def buggy_4(G, nodes=None):
    cliques = list(nx.find_cliques(G))
    # Bug: Misleading the base function by adding a non-existing node in the graph, this will result in ValueError and hence violates the inclusiveness property
    if nodes and len(nodes) > 0:
        return list(nx.find_cliques(G, nodes + ['non_existing_node'])) 
    return cliques

def buggy_5(G, nodes=None):
    cliques = list(nx.find_cliques(G))
    # Bug: Removing last element from each clique. If 'nodes' are at the end of the clique, it would result in violation of inclusiveness property
    for clique in cliques:
        if clique:
            clique.pop()
    return cliques