from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import large_clique_size

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=0, max_size=100))
def test_large_clique_size_non_negative_integer(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    clique_size = large_clique_size(G)
    assert clique_size >= 0

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=0, max_size=100))
def test_large_clique_size_not_exceeding_node_count(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    clique_size = large_clique_size(G)
    assert clique_size <= len(graph_nodes)

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=0, max_size=0))
def test_large_clique_size_empty_graph(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    clique_size = large_clique_size(G)
    assert clique_size == 0

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=100))
def test_large_clique_size_bounded_by_max_degree(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    G.add_edges_from([(i, j) for i in range(len(graph_nodes)) for j in range(i + 1, len(graph_nodes))])
    max_degree = max(dict(G.degree()).values())
    clique_size = large_clique_size(G)
    assert clique_size <= max_degree + 1

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, max_size=100))
def test_large_clique_size_disconnected_graph(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    # Create disconnected components
    for i in range(0, len(graph_nodes), 2):
        if i + 1 < len(graph_nodes):
            G.add_edge(graph_nodes[i], graph_nodes[i + 1])
    clique_size = large_clique_size(G)
    assert clique_size <= max(2, len(graph_nodes) // 2)

# End program