from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import large_clique_size

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=0, max_size=100).map(nx.path_graph))
def test_large_clique_size_non_negative_integer(G):
    k = large_clique_size(G)
    assert k >= 0

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=0, max_size=100).map(nx.path_graph))
def test_large_clique_size_not_exceeding_node_count(G):
    k = large_clique_size(G)
    assert k <= G.number_of_nodes()

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=0, max_size=0).map(nx.path_graph))
def test_large_clique_size_empty_graph(G):
    k = large_clique_size(G)
    assert k == 0

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=100).map(nx.path_graph))
def test_large_clique_size_not_exceeding_max_degree(G):
    k = large_clique_size(G)
    max_degree = max(dict(G.degree()).values(), default=0)
    assert k <= max_degree + 1

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=100).map(nx.connected_watts_strogatz_graph))
def test_large_clique_size_disconnected_components(G):
    k = large_clique_size(G)
    largest_clique_in_components = max(large_clique_size(G.subgraph(c)) for c in nx.connected_components(G))
    assert k <= largest_clique_in_components

# End program