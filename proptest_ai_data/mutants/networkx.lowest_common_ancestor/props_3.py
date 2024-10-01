import networkx as nx

def buggy_1(G, node1, node2, default=None):
    # Buggy version, always returns the default value
    result = nx.lowest_common_ancestor(G, node1, node2, default)
    return default

def buggy_2(G, node1, node2, default=None):
    # Buggy version that adds 1 to the returned ancestor node (if it exists)
    result = nx.lowest_common_ancestor(G, node1, node2, default)
    if result is not None:
        return result + 1
    else:
        return result

def buggy_3(G, node1, node2, default=None):
    # Buggy version that always returns node1 as lowest common ancestor
    result = nx.lowest_common_ancestor(G, node1, node2, default)
    return node1

def buggy_4(G, node1, node2, default=None):
    # Buggy version that always returns node2 as lowest common ancestor
    result = nx.lowest_common_ancestor(G, node1, node2, default)
    return node2

def buggy_5(G, node1, node2, default=None):
    # Buggy version that inverts the order of node1 and node2 in the networkx.lowest_common_ancestor call, 
    # might affect the results for directed graphs.
    result = nx.lowest_common_ancestor(G, node2, node1, default)
    return result