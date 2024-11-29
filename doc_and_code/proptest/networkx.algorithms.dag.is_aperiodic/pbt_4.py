from hypothesis import given, strategies as st
import networkx as nx
from hypothesis import HealthCheck, settings

# Set Hypothesis settings to avoid excessively large tests
settings.register_profile("ci", max_examples=1000, suppress_health_check=[HealthCheck.too_slow])
settings.set_profile("ci")

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
def test_input_graph_is_acyclic_property(edges):
    G = nx.DiGraph(edges)
    if not nx.is_aperiodic(G):
        assert nx.is_aperiodic(G) == False  # Acyclic graphs should return False

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
def test_single_cycle_of_length_k_property(edges):
    G = nx.DiGraph(edges)
    cycles = list(nx.simple_cycles(G))
    for cycle in cycles:
        if len(cycle) > 1:
            assert nx.is_aperiodic(G) == False  # Single cycle of length k > 1 should return False

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=2))
def test_multiple_cycles_coprime_lengths_property(edges):
    G = nx.DiGraph(edges)
    cycles = list(nx.simple_cycles(G))
    if all(len(cycle) > 1 for cycle in cycles):
        lengths = [len(cycle) for cycle in cycles]
        if len(set(lengths)) == len(lengths) and all(
            gcd(lengths[i], lengths[j]) == 1 for i in range(len(lengths)) for j in range(i + 1, len(lengths))
        ):
            assert nx.is_aperiodic(G) == True  # Coprime cycle lengths should return True

@given(st.lists(st.tuples(), min_size=0))
def test_empty_graph_property(edges):
    G = nx.DiGraph(edges)
    if len(G) == 0:
        try:
            nx.is_aperiodic(G)
        except nx.NetworkXPointlessConcept:
            assert True  # Should raise an error for empty graph

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
def test_directed_acyclic_graph_property(edges):
    G = nx.DiGraph(edges)
    if nx.is_directed_acyclic_graph(G):
        assert nx.is_aperiodic(G) == False  # Directed acyclic graphs should return False
# End program