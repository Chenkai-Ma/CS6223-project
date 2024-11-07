from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import large_clique_size

@given(st.data())
def test_large_clique_size_non_negative():
    G = st.one_of(
        st.builds(nx.complete_graph, st.integers(min_value=1, max_value=10)),
        st.builds(nx.empty_graph, st.integers(min_value=0, max_value=10))
    ).example()
    k = large_clique_size(G)
    assert k >= 0

@given(st.data())
def test_large_clique_size_within_node_count():
    num_nodes = st.integers(min_value=1, max_value=1000).example()
    G = nx.complete_graph(num_nodes)
    k = large_clique_size(G)
    assert k <= num_nodes

@given(st.data())
def test_large_clique_size_empty_graph():
    G = nx.empty_graph(0)
    k = large_clique_size(G)
    assert k == 0

@given(st.data())
def test_large_clique_size_bounded_by_max_degree():
    num_nodes = st.integers(min_value=1, max_value=10).example()
    G = nx.random_graphs.barabasi_albert_graph(num_nodes, 1)
    max_degree = max(dict(G.degree()).values())
    k = large_clique_size(G)
    assert k <= max_degree + 1

@given(st.data())
def test_large_clique_size_connected_components():
    G = nx.disjoint_union(nx.complete_graph(3), nx.complete_graph(4))
    k = large_clique_size(G)
    assert k == 4  # The largest clique is from the component with 4 nodes
# End program