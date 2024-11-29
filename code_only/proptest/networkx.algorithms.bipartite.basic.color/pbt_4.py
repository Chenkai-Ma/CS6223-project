from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.bipartite.basic import color

@given(st.data())
def test_output_contains_two_colors_property(data):
    # Generate a bipartite graph
    G = nx.bipartite.random_graph(10, 10)
    result = color(G)
    assert set(result.values()) == {0, 1}

@given(st.data())
def test_empty_graph_output_property(data):
    # Test for an empty graph
    G = nx.Graph()
    result = color(G)
    assert result == {}

@given(st.data())
def test_isolated_nodes_colored_zero_property(data):
    # Generate a graph with isolated nodes
    G = nx.Graph()
    G.add_nodes_from(range(5))
    G.add_edges_from([(0, 1), (1, 2)])  # 3 is isolated
    result = color(G)
    assert result[3] == 0

@given(st.data())
def test_one_to_one_mapping_property(data):
    # Generate a random bipartite graph
    G = nx.bipartite.random_graph(10, 10)
    result = color(G)
    assert len(result) == G.number_of_nodes()

@given(st.data())
def test_not_bipartite_graph_raises_error_property(data):
    # Generate a non-bipartite graph
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0)])  # Triangle (not bipartite)
    try:
        color(G)
        assert False, "Expected NetworkXError not raised"
    except nx.NetworkXError:
        pass
# End program