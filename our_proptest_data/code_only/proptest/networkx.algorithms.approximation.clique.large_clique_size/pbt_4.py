from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_large_clique_size_non_negative_property(data):
    G = data.draw(st.one_of(st.graphs(), st.sets(st.integers(min_value=0, max_value=100))))
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result >= 0

@given(st.data())
def test_large_clique_size_not_exceed_node_count_property(data):
    G = data.draw(st.graphs())
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result <= G.number_of_nodes()

@given(st.data())
def test_large_clique_size_empty_graph_property(data):
    G = nx.Graph()  # Create an empty graph
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result == 0

@given(st.data())
def test_large_clique_size_max_degree_property(data):
    G = data.draw(st.graphs())
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    max_degree = max(dict(G.degree()).values(), default=0)
    assert result <= max_degree + 1

@given(st.data())
def test_large_clique_size_isolated_nodes_property(data):
    G = nx.Graph()
    G.add_nodes_from(data.draw(st.lists(st.integers(), min_size=1)))
    result = nx.algorithms.approximation.clique.large_clique_size(G)
    assert result == 0
# End program