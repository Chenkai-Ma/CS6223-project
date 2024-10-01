import networkx as nx
import random

def buggy_1(G, node1, node2, default=None):
    result = nx.lowest_common_ancestor(G, node1, node2, default)
    # Bug: randomly add small amount of noise to the result.
    return result + random.randint(-1,1) if result is not None else result

def buggy_2(G, node1, node2, default=None):
    result = nx.lowest_common_ancestor(G, node1, node2, default)
    # Bug: switch the inputs in second call
    return nx.lowest_common_ancestor(G, node2, node1, default)

def buggy_3(G, node1, node2, default=None):
    result = nx.lowest_common_ancestor(G, node1, node2, default)
    # Bug: return the max of result and node1
    return max(result, node1) if result is not None else result

def buggy_4(G, node1, node2, default=None):
    result = nx.lowest_common_ancestor(G, node1, node2, default)
    # Bug: Return None for even node values.
    if result is not None and result % 2 == 0:
        return None
    return result

def buggy_5(G, node1, node2, default=None):
    result = nx.lowest_common_ancestor(G, node1, node2, default)
    # Bug: Return None when result equals node1 or node2.
    if result is not None and (node1 == result or node2 == result):
        return None
    return result