from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import bipartite
from networkx.exception import NetworkXError

@given(st.data())
def test_output_size_property(data):
    # Generate a bipartite graph
    G = nx.bipartite.random_graph(10, 10, p=0.5)
    c = bipartite.color(G)
    assert len(c) == len(G.nodes)

@given(st.data())
def test_color_values_property(data):
    # Generate a bipartite graph
    G = nx.bipartite.random_graph(10, 10, p=0.5)
    c = bipartite.color(G)
    assert all(color in [0, 1] for color in c.values())

@given(st.data())
def test_adjacent_nodes_different_colors_property(data):
    # Generate a bipartite graph
    G = nx.bipartite.random_graph(10, 10, p=0.5)
    c = bipartite.color(G)
    for u, v in G.edges:
        assert c[u] != c[v]

@given(st.data())
def test_valid_bipartite_coloring_property(data):
    # Generate a bipartite graph
    G = nx.bipartite.random_graph(10, 10, p=0.5)
    c = bipartite.color(G)
    for u, v in G.edges:
        assert c[u] != c[v]

@given(st.data())
def test_non_bipartite_graph_raises_exception_property(data):
    # Generate a non-bipartite graph
    G = nx.complete_graph(3)  # A triangle is not bipartite
    try:
        bipartite.color(G)
        assert False  # Should not reach this line
    except NetworkXError:
        assert True  # Exception was raised as expected
# End program