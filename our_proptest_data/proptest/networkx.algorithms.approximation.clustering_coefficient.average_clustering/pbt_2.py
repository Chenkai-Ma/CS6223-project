from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import approximation

@given(st.data())
def test_average_clustering_coefficient_float_range_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.erdos_renyi_graph, st.integers(min_value=0, max_value=100), st.floats(min_value=0, max_value=1)),
        st.builds(nx.complete_graph, st.integers(min_value=1, max_value=10)),
        st.builds(nx.empty_graph, st.integers(min_value=0, max_value=10))
    ))
    result = approximation.average_clustering(G)
    assert isinstance(result, float) and 0 <= result <= 1

@given(st.data())
def test_average_clustering_coefficient_no_edges_property(data):
    G = nx.empty_graph(5)  # A graph with no edges
    result = approximation.average_clustering(G)
    assert result == 0.0

@given(st.data())
def test_average_clustering_coefficient_consistency_property(data):
    G = data.draw(st.builds(nx.erdos_renyi_graph, st.integers(min_value=1, max_value=100), st.floats(min_value=0, max_value=1)))
    result1 = approximation.average_clustering(G, trials=10000)
    result2 = approximation.average_clustering(G, trials=10000)
    assert abs(result1 - result2) < 0.01  # Check for stability

@given(st.data())
def test_average_clustering_coefficient_empty_graph_property(data):
    G = nx.empty_graph(0)  # An empty graph
    result = approximation.average_clustering(G)
    assert result == 0.0

@given(st.data())
def test_average_clustering_coefficient_edge_addition_property(data):
    G = nx.erdos_renyi_graph(10, 0.5, seed=42)
    initial_clustering = approximation.average_clustering(G)
    
    # Add an edge and compute the new clustering
    G.add_edge(0, 1)
    new_clustering = approximation.average_clustering(G)
    
    assert new_clustering >= initial_clustering

# End program