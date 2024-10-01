import networkx as nx

def buggy_1(G, node1, node2, default=None):
    # introduce off-by-one error to the output
    return nx.lowest_common_ancestor(G, node1, node2, default) + 1

def buggy_2(G, node1, node2, default=None):
    # return one of the input nodes instead of lowest common ancestor
    return node1

def buggy_3(G, node1, node2, default=None):
    # return the inverse of the actual lowest common ancestor
    return -nx.lowest_common_ancestor(G, node1, node2, default)

def buggy_4(G, node1, node2, default=None):
    # return the sum of input nodes instead of lowest common ancestor
    return node1 + node2

def buggy_5(G, node1, node2, default=None):
    # ignore the computation and return a constant
    return 0