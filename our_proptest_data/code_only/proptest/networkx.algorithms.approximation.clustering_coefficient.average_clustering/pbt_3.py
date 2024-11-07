from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import average_clustering

@given(st.data())
def test_average_clustering_non_negative_property(data):
    G = nx.gnp_random_graph(data.draw(st.integers(min_value=0, max_value=1000)),
                             data.draw(st.floats(min_value=0.0, max_value=1.0)))
    result = average_clustering(G)
    assert result >= 0

@given(st.data())
def test_average_clustering_bounded_by_one_property(data):
    G = nx.gnp_random_graph(data.draw(st.integers(min_value=0, max_value=1000)),
                             data.draw(st.floats(min_value=0.0, max_value=1.0)))
    result = average_clustering(G)
    assert result <= 1

@given(st.data())
def test_average_clustering_empty_graph_property(data):
    G = nx.Graph()
    result = average_clustering(G)
    assert result == 0

@given(st.data())
def test_average_clustering_consistency_property(data):
    G = nx.gnp_random_graph(data.draw(st.integers(min_value=0, max_value=1000)),
                             data.draw(st.floats(min_value=0.0, max_value=1.0)))
    seed = data.draw(st.integers(min_value=0, max_value=10000))
    result1 = average_clustering(G, seed=seed)
    result2 = average_clustering(G, seed=seed)
    assert result1 == result2

@given(st.data())
def test_average_clustering_invariance_property(data):
    G = nx.gnp_random_graph(data.draw(st.integers(min_value=0, max_value=1000)),
                             data.draw(st.floats(min_value=0.0, max_value=1.0)))
    result1 = average_clustering(G)
    result2 = average_clustering(G.reverse())
    assert result1 == result2
# End program