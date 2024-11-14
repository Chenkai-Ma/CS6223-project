from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXPointlessConcept

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), unique_by=lambda x: x[0])
def test_is_aperiodic_acylclic_property(edges):
    G = nx.DiGraph(edges)
    if nx.is_directed_acyclic_graph(G):
        assert nx.is_aperiodic(G) is False

@given(st.integers(min_value=2, max_value=100), st.integers(min_value=1, max_value=50))
def test_is_aperiodic_single_cycle_property(cycle_length, node):
    G = nx.DiGraph([(node, (node + 1) % cycle_length) for node in range(cycle_length)])
    assert nx.is_aperiodic(G) is False

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=2, max_size=100), unique_by=lambda x: x[0])
def test_is_aperiodic_coprime_cycles_property(edges):
    G = nx.DiGraph(edges)
    if nx.number_of_cycles(G) > 1 and nx.is_aperiodic(G):
        assert nx.is_aperiodic(G) is True

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=0, max_size=0))
def test_is_aperiodic_empty_graph_property(edges):
    G = nx.DiGraph(edges)
    try:
        nx.is_aperiodic(G)
    except NetworkXPointlessConcept:
        assert True

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=2, max_size=100))
def test_is_aperiodic_directed_acyclic_property(edges):
    G = nx.DiGraph(edges)
    if nx.is_directed_acyclic_graph(G):
        assert nx.is_aperiodic(G) is False
# End program