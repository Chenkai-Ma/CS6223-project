from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXError

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_acyclic_graph_property(edges):
    G = nx.DiGraph(edges)
    if nx.is_directed_acyclic_graph(G):
        assert nx.algorithms.dag.is_aperiodic(G) is False

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_single_cycle_property(edges):
    if len(edges) == 2 and edges[0][0] == edges[1][1]:  # Ensuring a single cycle
        G = nx.DiGraph(edges)
        cycle_length = len(edges)
        if cycle_length > 1:
            assert nx.algorithms.dag.is_aperiodic(G) is False

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=3, max_size=100))
def test_coprime_cycles_property(edges):
    G = nx.DiGraph(edges)
    if nx.is_strongly_connected(G):
        cycle_lengths = {len(cycle) for cycle in nx.simple_cycles(G)}
        if len(cycle_lengths) > 1 and all(cycle_lengths):
            assert gcd(*cycle_lengths) == 1
            assert nx.algorithms.dag.is_aperiodic(G) is True

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=4, max_size=100))
def test_common_divisor_cycles_property(edges):
    G = nx.DiGraph(edges)
    if nx.is_strongly_connected(G):
        cycle_lengths = {len(cycle) for cycle in nx.simple_cycles(G)}
        if len(cycle_lengths) > 1 and all(cycle_lengths):
            common_divisor = gcd(*cycle_lengths)
            if common_divisor > 1:
                assert nx.algorithms.dag.is_aperiodic(G) is False

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_order_independence_property(edges):
    G1 = nx.DiGraph(edges)
    G2 = nx.DiGraph(edges[::-1])  # Reverse the edges
    assert nx.algorithms.dag.is_aperiodic(G1) == nx.algorithms.dag.is_aperiodic(G2)

# End program