from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation.clique import large_clique_size

@given(st.data())
def test_output_is_non_negative_property(data):
    G = data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=0).map(nx.Graph))
    result = large_clique_size(G)
    assert result >= 0

@given(st.data())
def test_output_does_not_exceed_node_count_property(data):
    G = data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=0).map(nx.Graph))
    result = large_clique_size(G)
    assert result <= G.number_of_nodes()

@given(st.data())
def test_output_zero_for_empty_graph_property(data):
    G = nx.Graph()  # An empty graph
    result = large_clique_size(G)
    assert result == 0

@given(st.data())
def test_output_within_max_degree_plus_one_property(data):
    G = data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1).map(nx.Graph))
    result = large_clique_size(G)
    max_degree = max(dict(G.degree()).values())
    assert result <= max_degree + 1

@given(st.data())
def test_output_zero_for_isolated_nodes_property(data):
    G = nx.Graph()
    isolated_nodes = data.draw(st.lists(st.integers(), min_size=1))
    G.add_nodes_from(isolated_nodes)  # Add isolated nodes
    result = large_clique_size(G)
    assert result == 0
# End program