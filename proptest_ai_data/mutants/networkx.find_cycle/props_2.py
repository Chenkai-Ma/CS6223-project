import networkx as nx
from typing import Union

def buggy_1(G: nx.Graph, source: Union[int, list] = None, orientation: str = None):
    edges = nx.find_cycle(G, source=source, orientation=orientation)
    if edges:
        # Remove the last edge, which violates the cycle property
        edges.pop()
    return edges


def buggy_2(G: nx.Graph, source: Union[int, list] = None, orientation: str = None):
    edges = nx.find_cycle(G, source=source, orientation=orientation)
    if edges:
        # Replace the last edge with a non-existent edge
        edges[-1] = (9999, 9999)
    return edges


def buggy_3(G: nx.Graph, source: Union[int, list] = None, orientation: str = None):
    edges = nx.find_cycle(G, source=source, orientation=orientation)
    if edges:
        # Reverse the order of edges
        edges = edges[::-1]
    return edges


def buggy_4(G: nx.Graph, source: Union[int, list] = None, orientation: str = None):
    edges = nx.find_cycle(G, source=source, orientation=orientation)
    if edges:
        # Add an extra edge
        edges.append((0, 0))
    return edges


def buggy_5(G: nx.Graph, source: Union[int, list] = None, orientation: str = None):
    edges = nx.find_cycle(G, source=source, orientation=orientation)
    if edges:
        # Modify the first edge
        edges[0] = (edges[0][0], 9999)
    return edges