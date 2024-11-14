from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_large_clique_size_non_negative_property(data):
    G = data.draw(st.sets(st.integers(min_size=1, max_size=100)).map(lambda nodes: nx.Graph(nx.complete_graph(nodes))))
    result = nx.approximation.large_clique_size(G)
    assert result >= 0

@given(st.data())
def test_large_clique_size_does_not_exceed_node_count_property(data):
    G = data.draw(st.sets(st.integers(min_size=1, max_size=100)).map(lambda nodes: nx.Graph(nx.complete_graph(nodes))))
    result = nx.approximation.large_clique_size(G)
    assert result <= G.number_of_nodes()

@given(st.data())
def test_large_clique_size_empty_graph_property(data):
    G = nx.Graph()  # Empty graph
    result = nx.approximation.large_clique_size(G)
    assert result == 0

@given(st.data())
def test_large_clique_size_at_least_one_edge_property(data):
    G = data.draw(st.sets(st.integers(min_size=2, max_size=100)).map(lambda nodes: nx.Graph(nx.complete_graph(nodes))))
    if G.number_of_edges() > 0:
        result = nx.approximation.large_clique_size(G)
        assert result >= 1

@given(st.data())
def test_large_clique_size_consistency_property(data):
    G = data.draw(st.sets(st.integers(min_size=1, max_size=100)).map(lambda nodes: nx.Graph(nx.complete_graph(nodes))))
    result1 = nx.approximation.large_clique_size(G)
    result2 = nx.approximation.large_clique_size(G)
    assert result1 == result2
# End program