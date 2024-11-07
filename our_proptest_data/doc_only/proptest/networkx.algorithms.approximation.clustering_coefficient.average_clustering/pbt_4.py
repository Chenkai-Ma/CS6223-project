from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import approximation

@given(st.data())
def test_average_clustering_output_range_property(data):
    G = data.draw(st.builds(nx.erdos_renyi_graph, st.integers(min_value=0, max_value=100), st.floats(min_value=0.0, max_value=1.0)))
    result = approximation.average_clustering(G, trials=1000)
    assert 0.0 <= result <= 1.0

@given(st.data())
def test_average_clustering_no_edges_property(data):
    G = nx.Graph()
    result = approximation.average_clustering(G, trials=1000)
    assert result == 0.0

@given(st.data())
def test_average_clustering_consistency_property(data):
    G = data.draw(st.builds(nx.erdos_renyi_graph, st.integers(min_value=5, max_value=20), st.floats(min_value=0.0, max_value=1.0)))
    result1 = approximation.average_clustering(G, trials=1000)
    result2 = approximation.average_clustering(G, trials=1000)
    assert abs(result1 - result2) < 0.1  # Allow some tolerance for approximation

@given(st.data())
def test_average_clustering_empty_graph_property(data):
    G = nx.Graph()
    result = approximation.average_clustering(G, trials=1000)
    assert result == 0.0

@given(st.data())
def test_average_clustering_structure_variation_property(data):
    G = data.draw(st.builds(nx.erdos_renyi_graph, st.integers(min_value=5, max_value=20), st.floats(min_value=0.0, max_value=1.0)))
    original_clustering = approximation.average_clustering(G, trials=1000)
    
    # Add an edge
    if G.number_of_edges() > 0:
        u, v = list(G.nodes())[:2]
        G.add_edge(u, v)
        new_clustering = approximation.average_clustering(G, trials=1000)
        assert new_clustering >= original_clustering

    # Remove an edge
    if G.number_of_edges() > 1:
        u, v = list(G.edges())[0]
        G.remove_edge(u, v)
        new_clustering = approximation.average_clustering(G, trials=1000)
        assert new_clustering <= original_clustering
# End program