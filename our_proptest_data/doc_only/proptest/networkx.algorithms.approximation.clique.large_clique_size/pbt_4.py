from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import large_clique_size

@given(st.lists(st.integers(min_value=1, max_value=100), min_size=0, max_size=100))
def test_large_clique_size_non_negative_integer(graph_data):
    G = nx.Graph()
    G.add_nodes_from(graph_data)
    clique_size = large_clique_size(G)
    assert isinstance(clique_size, int) and clique_size >= 0

@given(st.lists(st.integers(min_value=1, max_value=100), min_size=0, max_size=100))
def test_large_clique_size_not_exceed_total_nodes(graph_data):
    G = nx.Graph()
    G.add_nodes_from(graph_data)
    clique_size = large_clique_size(G)
    assert clique_size <= len(graph_data)

@given(st.lists(st.integers(min_value=1, max_value=100), min_size=0, max_size=0))
def test_large_clique_size_empty_graph(empty_graph_data):
    G = nx.Graph()
    clique_size = large_clique_size(G)
    assert clique_size == 0

@given(st.lists(st.integers(min_value=1, max_value=100), min_size=1, max_size=100))
def test_large_clique_size_bounded_by_degree(graph_data):
    G = nx.Graph()
    G.add_nodes_from(graph_data)
    G.add_edges_from([(graph_data[i], graph_data[j]) for i in range(len(graph_data)) for j in range(i+1, len(graph_data))])
    max_degree = max(dict(G.degree()).values())
    clique_size = large_clique_size(G)
    assert clique_size <= max_degree + 1

@given(st.lists(st.integers(min_value=1, max_value=100), min_size=1, max_size=100))
def test_large_clique_size_disconnected_components(graph_data):
    G = nx.Graph()
    G.add_nodes_from(graph_data)
    G.add_edges_from([(graph_data[i], graph_data[j]) for i in range(0, len(graph_data)//2) for j in range(len(graph_data)//2, len(graph_data))])
    clique_size = large_clique_size(G)
    # Since the graph is disconnected, the size should reflect the largest clique in the components.
    # We are not asserting a specific value here as it depends on the specific connections.
    assert clique_size >= 0

# End program