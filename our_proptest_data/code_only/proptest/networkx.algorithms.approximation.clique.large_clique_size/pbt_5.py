from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation.clique import large_clique_size

@given(st.data())
def test_large_clique_size_non_negative_property(data):
    G = data.draw(st.shapes.basic_graphs())
    result = large_clique_size(G)
    assert result >= 0  # Output should be a non-negative integer

@given(st.data())
def test_large_clique_size_not_exceed_node_count_property(data):
    G = data.draw(st.shapes.basic_graphs())
    result = large_clique_size(G)
    assert result <= len(G.nodes)  # Output should not exceed the number of nodes

@given(st.data())
def test_large_clique_size_empty_graph_property(data):
    G = nx.Graph()  # Create an empty graph
    result = large_clique_size(G)
    assert result == 0  # Output should be zero for an empty graph

@given(st.data())
def test_large_clique_size_max_degree_property(data):
    G = data.draw(st.shapes.basic_graphs())
    result = large_clique_size(G)
    max_degree = max(dict(G.degree).values(), default=0)
    assert result <= max_degree + 1  # Output should not exceed max degree + 1

@given(st.data())
def test_large_clique_size_isolated_nodes_property(data):
    G = nx.Graph()
    G.add_nodes_from(data.draw(st.lists(st.integers(), min_size=1, max_size=100)))  # Add isolated nodes
    result = large_clique_size(G)
    assert result == 0  # Output should be zero for a graph with only isolated nodes
# End program