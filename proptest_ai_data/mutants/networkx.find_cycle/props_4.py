import networkx as nx

def buggy_1(G, source=None, orientation=None):
    # returns a list instead of a list of tuples
    result = nx.find_cycle(G, source, orientation)
    return [item for tup in result for item in tup]

def buggy_2(G, source=None, orientation=None):
    # returns a list of tuples, but all tuples have only one element irrespective of the graph type
    result = nx.find_cycle(G, source, orientation)
    return [(edge[0],) for edge in result]

def buggy_3(G, source=None, orientation=None):
    # returns a list of tuples, but the tuples have four elements even if the graph is not a multigraph
    result = nx.find_cycle(G, source, orientation)
    return [(edge[0], edge[1], 'extra', 'extra') for edge in result]

def buggy_4(G, source=None, orientation=None):
    # returns a list of tuples, but the direction of traversal is not included even if orientation is not None
    result = nx.find_cycle(G, source, 'original')
    if isinstance(G, nx.MultiGraph):
        return [(edge[0], edge[1], edge[2]) for edge in result]
    else:
        return [(edge[0], edge[1]) for edge in result]

def buggy_5(G, source=None, orientation=None):
    # returns a list of tuples, but the direction of traversal is added even if orientation is None
    result = nx.find_cycle(G, source, None)
    return [(edge[0], edge[1], 'forward') for edge in result]