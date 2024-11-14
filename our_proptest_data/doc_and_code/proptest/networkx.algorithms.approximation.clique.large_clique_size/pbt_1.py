from hypothesis import given, strategies as st
import networkx as nx
from hypothesis import strategies as st

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=0, max_size=100).map(set).map(lambda nodes: nx.Graph(nx.path_graph(nodes))), 
                )
def test_large_clique_size_non_negative_integer_property(G):
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result >= 0

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=0, max_size=100).map(set).map(lambda nodes: nx.Graph(nx.path_graph(nodes))), 
                )
def test_large_clique_size_within_node_count_property(G):
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result <= G.number_of_nodes()

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=0, max_size=0).map(set).map(lambda nodes: nx.Graph(nx.path_graph(nodes))), 
                )
def test_large_clique_size_empty_graph_property(G):
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result == 0

@given(st.lists(st.integers(min_value=1, max_value=100), min_size=1, max_size=100).map(set).map(lambda nodes: nx.Graph(nx.path_graph(nodes))), 
                )
def test_large_clique_size_at_least_one_edge_property(G):
    if G.number_of_edges() > 0:
        result = nx.algorithms.approximation.clique.large_clique_size(G)
        assert result >= 1

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=100).map(set).map(lambda nodes: nx.Graph(nx.path_graph(nodes))), 
                )
def test_large_clique_size_consistent_output_property(G):
    result1 = nx.algorithms.approximation.clique.large_clique_size(G)
    result2 = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result1 == result2
# End program