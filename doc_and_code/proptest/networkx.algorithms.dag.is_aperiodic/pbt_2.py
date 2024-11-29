from hypothesis import given, strategies as st
import networkx as nx
from hypothesis.strategies import integers, lists

@given(st.data())
def test_is_aperiodic_property_acyclic_graph():
    # Generate a directed acyclic graph
    nodes = st.lists(st.integers(min_value=1, max_value=100), min_size=1, max_size=10).example()
    edges = st.lists(st.tuples(st.sampled_from(nodes), st.sampled_from(nodes))).filter(lambda x: not any(v == u for u, v in x)).example()
    G = nx.DiGraph(edges)
    assert nx.is_aperiodic(G) is False

@given(st.data())
def test_is_aperiodic_property_single_cycle():
    # Generate a directed graph with a single cycle of length k > 1
    k = st.integers(min_value=2, max_value=10).example()
    nodes = list(range(1, k + 1))
    edges = [(i, i + 1) for i in nodes[:-1]] + [(k, 1)]
    G = nx.DiGraph(edges)
    assert nx.is_aperiodic(G) is False

@given(st.data())
def test_is_aperiodic_property_coprime_cycles():
    # Generate a directed graph with coprime cycle lengths
    cycle1_length = st.integers(min_value=2, max_value=10).example()
    cycle2_length = st.integers(min_value=11, max_value=20).filter(lambda x: x % cycle1_length != 0).example()
    
    nodes = list(range(1, cycle1_length + cycle2_length + 1))
    edges = [(i, i + 1) for i in range(1, cycle1_length)] + [(cycle1_length, 1)]  # First cycle
    edges += [(i + cycle1_length, i + cycle1_length + 1) for i in range(1, cycle2_length)] + [(cycle1_length + cycle2_length, cycle1_length + 1)]
    
    G = nx.DiGraph(edges)
    assert nx.is_aperiodic(G) is True

@given(st.data())
def test_is_aperiodic_property_empty_graph():
    # Test with an empty graph
    G = nx.DiGraph()
    try:
        nx.is_aperiodic(G)
        assert False, "Expected a NetworkXPointlessConcept error for empty graph"
    except nx.NetworkXPointlessConcept:
        pass

@given(st.data())
def test_is_aperiodic_property_directed_acyclic_graph():
    # Generate a directed acyclic graph
    nodes = st.lists(st.integers(min_value=1, max_value=100), min_size=1, max_size=10).example()
    edges = st.lists(st.tuples(st.sampled_from(nodes), st.sampled_from(nodes))).filter(lambda x: not any(v == u for u, v in x)).example()
    G = nx.DiGraph(edges)
    assert nx.is_aperiodic(G) is False
# End program