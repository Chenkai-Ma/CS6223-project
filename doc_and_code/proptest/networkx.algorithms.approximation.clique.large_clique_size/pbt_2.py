from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_large_clique_size_non_negative_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.path_graph, st.integers(min_value=0, max_value=100)),
        st.builds(nx.complete_graph, st.integers(min_value=1, max_value=10))
    ))
    result = nx.approximation.large_clique_size(G)
    assert result >= 0

@given(st.data())
def test_large_clique_size_not_exceed_node_count_property(data):
    num_nodes = data.draw(st.integers(min_value=0, max_value=100))
    G = nx.complete_graph(num_nodes)
    result = nx.approximation.large_clique_size(G)
    assert result <= num_nodes

@given(st.data())
def test_large_clique_size_empty_graph_property(data):
    G = nx.empty_graph(0)
    result = nx.approximation.large_clique_size(G)
    assert result == 0

@given(st.data())
def test_large_clique_size_at_least_one_for_non_empty_graph_property(data):
    num_nodes = data.draw(st.integers(min_value=1, max_value=100))
    G = nx.complete_graph(num_nodes)
    result = nx.approximation.large_clique_size(G)
    assert result >= 1

@given(st.data())
def test_large_clique_size_consistency_property(data):
    num_nodes = data.draw(st.integers(min_value=1, max_value=100))
    G = nx.complete_graph(num_nodes)
    result1 = nx.approximation.large_clique_size(G)
    result2 = nx.approximation.large_clique_size(G)
    assert result1 == result2
# End program