import networkx as nx
import time

def buggy_1(G, node1, node2, default=None):
    # Introduces an infinite loop, causing infinite wait
    while True:
        continue
    return nx.lowest_common_ancestor(G, node1, node2, default)

def buggy_2(G, node1, node2, default=None):
    # Introduces potential deadlock through sleep
    time.sleep(1000)
    return nx.lowest_common_ancestor(G, node1, node2, default)

def buggy_3(G, node1, node2, default=None):
    # Always return default, ignoring the common ancestor
    return default

def buggy_4(G, node1, node2, default=None):
    # Returns None regardless of the actual common ancestor
    return None

def buggy_5(G, node1, node2, default=None):
    # Returns a random node, not necessarily the common ancestor
    return list(G.nodes())[0]