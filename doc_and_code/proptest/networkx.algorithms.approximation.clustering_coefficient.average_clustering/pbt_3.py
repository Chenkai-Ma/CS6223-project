from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import approximation

@given(st.lists(st.tuples(st.integers(min_value=0, max_value=100), st.integers(min_value=0, max_value=100)), min_size=1), min_size=1)
def test_output_between_0_and_1_property(graph_edges):
    G = nx.Graph()
    G.add_edges_from(graph_edges)
    result = approximation.average_clustering(G, trials=1000)
    assert 0 <= result <= 1

@given(st.lists(st.tuples(st.integers(min_value=0, max_value=100), st.integers(min_value=0, max_value=100)), min_size=1), min_size=1)
def test_output_zero_for_no_edges_property(graph_edges):
    G = nx.Graph()
    G.add_edges_from(graph_edges)
    if len(G.edges) == 0 or all(len(list(G.neighbors(n))) < 2 for n in G.nodes):
        result = approximation.average_clustering(G, trials=1000)
        assert result == 0

@given(st.lists(st.tuples(st.integers(min_value=0, max_value=100), st.integers(min_value=0, max_value=100)), min_size=1), st.integers(min_value=0, max_value=100))
def test_reproducibility_with_fixed_seed_property(graph_edges, seed):
    G = nx.Graph()
    G.add_edges_from(graph_edges)
    result1 = approximation.average_clustering(G, trials=1000, seed=seed)
    result2 = approximation.average_clustering(G, trials=1000, seed=seed)
    assert result1 == result2

@given(st.lists(st.tuples(st.integers(min_value=0, max_value=100), st.integers(min_value=0, max_value=100)), min_size=1), st.integers(min_value=0, max_value=100))
def test_approximation_convergence_property(graph_edges, trials):
    G = nx.Graph()
    G.add_edges_from(graph_edges)
    deterministic_result = nx.average_clustering(G)
    result = approximation.average_clustering(G, trials=trials)
    assert abs(result - deterministic_result) < 0.1  # Allow some margin of error

@given(st.lists(st.tuples(st.integers(min_value=0, max_value=100), st.integers(min_value=0, max_value=100)), min_size=1), min_size=1)
def test_directed_graph_exception_property(graph_edges):
    G = nx.DiGraph()
    G.add_edges_from(graph_edges)
    try:
        approximation.average_clustering(G, trials=1000)
        assert False, "Expected NetworkXNotImplemented exception for directed graph"
    except nx.NetworkXNotImplemented:
        pass
# End program