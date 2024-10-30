from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.dag import is_aperiodic

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=20))
def test_acyclic_graph_property(edges):
    G = nx.DiGraph(edges)
    if nx.is_directed_acyclic_graph(G):
        assert is_aperiodic(G) is False

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=2, max_size=20))
def test_single_cycle_property(edges):
    G = nx.DiGraph(edges)
    cycles = list(nx.simple_cycles(G))
    if len(cycles) == 1 and len(cycles[0]) > 1:
        assert is_aperiodic(G) is False

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=3, max_size=20))
def test_coprime_cycles_property(edges):
    G = nx.DiGraph(edges)
    cycles = list(nx.simple_cycles(G))
    cycle_lengths = [len(cycle) for cycle in cycles]
    if len(cycle_lengths) > 1 and all(nx.gcd(cycle_lengths) == 1):
        assert is_aperiodic(G) is True

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=4, max_size=20))
def test_common_divisor_cycles_property(edges):
    G = nx.DiGraph(edges)
    cycles = list(nx.simple_cycles(G))
    cycle_lengths = [len(cycle) for cycle in cycles]
    if len(cycle_lengths) > 1 and not all(nx.gcd(cycle_lengths) == 1):
        assert is_aperiodic(G) is False

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=20))
def test_order_independence_property(edges):
    G1 = nx.DiGraph(edges)
    G2 = nx.DiGraph(sorted(edges))  # Sort edges to create a different order
    assert is_aperiodic(G1) == is_aperiodic(G2)

# End program