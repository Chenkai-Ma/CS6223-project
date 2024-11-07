from hypothesis import given, strategies as st
import networkx as nx
from hypothesis import settings

# Setting a reasonable limit for performance and to avoid very large inputs
settings.max_examples = 100

@given(st.data())
def test_average_clustering_non_negative_property(data):
    G = data.draw(st.builds(nx.gnm_random_graph, st.integers(0, 100), st.integers(0, 500)))
    result = nx.algorithms.approximation.clustering_coefficient.average_clustering(G)
    assert result >= 0

@given(st.data())
def test_average_clustering_upper_bound_property(data):
    G = data.draw(st.builds(nx.gnm_random_graph, st.integers(0, 100), st.integers(0, 500)))
    result = nx.algorithms.approximation.clustering_coefficient.average_clustering(G)
    assert result <= 1

@given(st.data())
def test_average_clustering_empty_graph_property(data):
    G = nx.Graph()  # Creating an empty graph
    result = nx.algorithms.approximation.clustering_coefficient.average_clustering(G)
    assert result == 0

@given(st.data())
def test_average_clustering_consistency_property(data):
    G = data.draw(st.builds(nx.gnm_random_graph, st.integers(0, 100), st.integers(0, 500)))
    seed = 42  # Fixed seed for consistency
    result_1 = nx.algorithms.approximation.clustering_coefficient.average_clustering(G, seed=seed)
    result_2 = nx.algorithms.approximation.clustering_coefficient.average_clustering(G, seed=seed)
    assert result_1 == result_2

@given(st.data())
def test_average_clustering_invariance_property(data):
    G = data.draw(st.builds(nx.gnm_random_graph, st.integers(0, 100), st.integers(0, 500)))
    result_1 = nx.algorithms.approximation.clustering_coefficient.average_clustering(G)
    G_reordered = nx.relabel_nodes(G, {n: n for n in G.nodes()})  # Relabeling nodes does not change the graph
    result_2 = nx.algorithms.approximation.clustering_coefficient.average_clustering(G_reordered)
    assert result_1 == result_2
# End program