import networkx as nx

def buggy_1(G, node1, node2, default=None):
    result = nx.lowest_common_ancestor(G, node1, node2, default=default)
    # Regardless of the result, always return None
    return None

def buggy_2(G, node1, node2, default=None):
    result = nx.lowest_common_ancestor(G, node1, node2, default=default)
    # Return the opposite - if result is None, return the default. If result is the default, return None.
    return default if result is None else None

def buggy_3(G, node1, node2, default=None):
    result = nx.lowest_common_ancestor(G, node1, node2, default=default)
    # Always return the first node instead of the default 
    return node1

def buggy_4(G, node1, node2, default=None):
    result = nx.lowest_common_ancestor(G, node1, node2, default=default)
    # Always return the second node instead of the default
    return node2

def buggy_5(G, node1, node2, default=None):
    result = nx.lowest_common_ancestor(G, node1, node2, default=default)
    # Returns the tuple (node1, node2) instead of default value
    return (node1, node2)