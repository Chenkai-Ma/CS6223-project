from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import average_clustering

@given(st.data())
def test_average_clustering_non_negative_property(data):
    G = data.draw(st.graphs())
    result = average_clustering(G)
    assert result >= 0

@given(st.data())
def test_average_clustering_upper_bound_property(data):
    G = data.draw(st.graphs())
    result = average_clustering(G)
    assert result <= 1

@given(st.data())
def test_average_clustering_empty_graph_property(data):
    G = nx.Graph()  # Create an empty graph
    result = average_clustering(G)
    assert result == 0

@given(st.data())
def test_average_clustering_consistency_property(data):
    G = data.draw(st.graphs())
    seed = data.draw(st.integers(min_value=0, max_value=1000))
    result1 = average_clustering(G, seed=seed)
    result2 = average_clustering(G, seed=seed)
    assert result1 == result2

@given(st.data())
def test_average_clustering_invariance_property(data):
    G = data.draw(st.graphs())
    result1 = average_clustering(G)
    G_reordered = nx.relabel_nodes(G, {n: n for n in G.nodes()})  # Label nodes to keep the structure
    result2 = average_clustering(G_reordered)
    assert result1 == result2
# End program