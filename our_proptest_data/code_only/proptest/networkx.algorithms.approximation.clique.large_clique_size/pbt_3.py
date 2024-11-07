from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_large_clique_size_output_non_negative():
    G = st.builds(nx.Graph, st.lists(st.integers(), min_size=1)).example()
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result >= 0

@given(st.data())
def test_large_clique_size_output_not_exceeding_node_count():
    G = st.builds(nx.Graph, st.lists(st.integers(), min_size=1)).example()
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result <= G.number_of_nodes()

@given(st.data())
def test_large_clique_size_empty_graph():
    G = nx.Graph()
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result == 0

@given(st.data())
def test_large_clique_size_output_bounded_by_max_degree():
    G = st.builds(nx.Graph, st.lists(st.integers(), min_size=1)).example()
    max_degree = max(dict(G.degree()).values(), default=0)
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result <= max_degree + 1

@given(st.data())
def test_large_clique_size_isolated_nodes():
    G = nx.Graph()
    isolated_nodes = st.lists(st.integers(), min_size=1).example()
    G.add_nodes_from(isolated_nodes)
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result == 0
# End program