from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.dag import is_aperiodic

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
def test_acyclic_graph_property(edges):
    # Create a directed graph from the edges
    G = nx.DiGraph(edges)
    # Check if the graph is acyclic
    if nx.is_directed_acyclic_graph(G):
        assert is_aperiodic(G) is False

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
def test_single_cycle_property(edges):
    # Create a directed graph from the edges
    G = nx.DiGraph(edges)
    # Find cycles in the graph
    cycles = list(nx.simple_cycles(G))
    for cycle in cycles:
        if len(cycle) > 1:
            assert is_aperiodic(G) is False

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
def test_coprime_cycles_property(edges):
    # Create a directed graph from the edges
    G = nx.DiGraph(edges)
    # Find cycles in the graph
    cycles = list(nx.simple_cycles(G))
    lengths = [len(cycle) for cycle in cycles]
    if len(lengths) > 1 and all(lengths[i] % lengths[j] != 0 for i in range(len(lengths)) for j in range(len(lengths)) if i != j):
        assert is_aperiodic(G) is True

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
def test_common_divisor_cycles_property(edges):
    # Create a directed graph from the edges
    G = nx.DiGraph(edges)
    # Find cycles in the graph
    cycles = list(nx.simple_cycles(G))
    lengths = [len(cycle) for cycle in cycles]
    if len(lengths) > 1 and any(lengths[i] % lengths[j] == 0 for i in range(len(lengths)) for j in range(len(lengths)) if i != j):
        assert is_aperiodic(G) is False

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
def test_edge_permutation_property(edges):
    # Create a directed graph from the edges
    G1 = nx.DiGraph(edges)
    G2 = nx.DiGraph(sorted(edges))  # Sort edges to create a permutation
    assert is_aperiodic(G1) == is_aperiodic(G2)
# End program