from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import clique

@given(st.data())
def test_large_clique_size_non_negative():
    G = st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1)).example()
    k = clique.large_clique_size(G)
    assert k >= 0  # Output must be a non-negative integer

@given(st.data())
def test_large_clique_size_does_not_exceed_node_count():
    G = st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1)).example()
    node_count = G.number_of_nodes()
    k = clique.large_clique_size(G)
    assert k <= node_count  # Output must not exceed total number of nodes

@given(st.data())
def test_large_clique_size_empty_graph():
    G = nx.Graph()  # Create an empty graph
    k = clique.large_clique_size(G)
    assert k == 0  # Output should be zero for empty graph

@given(st.data())
def test_large_clique_size_bounded_by_max_degree():
    G = st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1)).example()
    max_degree = max(dict(G.degree()).values(), default=0)
    k = clique.large_clique_size(G)
    assert k <= max_degree + 1  # Output must be less than or equal to max degree + 1

@given(st.data())
def test_large_clique_size_disconnected_graph():
    G = st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1)).example()
    components = list(nx.connected_components(G))
    largest_clique_size = max(clique.large_clique_size(G.subgraph(comp)) for comp in components)
    k = clique.large_clique_size(G)
    assert k == largest_clique_size  # Output should reflect the largest clique in any component
# End program