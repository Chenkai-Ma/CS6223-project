from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import approximation

@given(st.data())
def test_output_range_property():
    G = nx.erdos_renyi_graph(10, 0.5)
    trials = st.integers(min_value=1, max_value=1000).example()
    result = approximation.average_clustering(G, trials=trials)
    assert 0 <= result <= 1

@given(st.data())
def test_zero_output_property():
    G = nx.Graph()
    trials = st.integers(min_value=1, max_value=1000).example()
    result = approximation.average_clustering(G, trials=trials)
    assert result == 0

@given(st.data())
def test_reproducibility_property():
    G = nx.erdos_renyi_graph(10, 0.5)
    trials = 1000
    seed = 42
    result1 = approximation.average_clustering(G, trials=trials, seed=seed)
    result2 = approximation.average_clustering(G, trials=trials, seed=seed)
    assert result1 == result2

@given(st.data())
def test_convergence_to_true_value_property():
    G = nx.erdos_renyi_graph(100, 0.5)
    trials = 10000
    result_approx = approximation.average_clustering(G, trials=trials)
    result_true = nx.average_clustering(G)
    assert abs(result_approx - result_true) < 0.05

@given(st.data())
def test_directed_graph_exception_property():
    G = nx.DiGraph()
    with pytest.raises(nx.NetworkXNotImplemented):
        approximation.average_clustering(G)
# End program