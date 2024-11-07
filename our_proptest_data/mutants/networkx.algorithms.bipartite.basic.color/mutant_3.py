# property to violate: Nodes that are directly connected by an edge in the graph \( G \) must have different color values in the output dictionary.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import bipartite

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_1():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Violate the property by setting all colors to 0
        for node in c:
            c[node] = 0
        for u, v in G.edges:
            assert c[u] != c[v]

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_2():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Violate the property by setting all colors to 1
        for node in c:
            c[node] = 1
        for u, v in G.edges:
            assert c[u] != c[v]

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_3():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Violate the property by making the color of one node the same as its neighbor
        for u, v in G.edges:
            c[v] = c[u]  # Set v's color to be the same as u's
        for u, v in G.edges:
            assert c[u] != c[v]

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_4():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Violate the property by duplicating colors
        colors = list(c.values())
        for node in c:
            c[node] = colors[0]  # Set all nodes to the same color
        for u, v in G.edges:
            assert c[u] != c[v]

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_5():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Violate the property by assigning the same color to all nodes
        for node in c:
            c[node] = 0 if node % 2 == 0 else 1  # Alternate colors but make sure adjacent nodes have the same color
        for u, v in G.edges:
            assert c[u] != c[v]