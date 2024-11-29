from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation.clustering_coefficient import average_clustering

@given(st.data())
def test_average_clustering_non_negative_property(data):
    graph = data.draw(st.connected_graphs(min_size=0))
    result = average_clustering(graph)
    assert result >= 0

@given(st.data())
def test_average_clustering_upper_bound_property(data):
    graph = data.draw(st.connected_graphs(min_size=1))
    result = average_clustering(graph)
    assert result <= 1

@given(st.data())
def test_average_clustering_empty_graph_property(data):
    graph = nx.Graph()  # Create an empty graph
    result = average_clustering(graph)
    assert result == 0

@given(st.data())
def test_average_clustering_consistency_property(data):
    graph = data.draw(st.connected_graphs(min_size=1))
    seed = data.draw(st.integers(min_value=0, max_value=1000))
    result_1 = average_clustering(graph, seed=seed)
    result_2 = average_clustering(graph, seed=seed)
    assert result_1 == result_2

@given(st.data())
def test_average_clustering_invariance_property(data):
    graph = data.draw(st.connected_graphs(min_size=1))
    result_1 = average_clustering(graph)
    result_2 = average_clustering(nx.relabel.relabel_nodes(graph, {n: n for n in graph.nodes()}))  # Same graph with relabeled nodes
    assert result_1 == result_2
# End program