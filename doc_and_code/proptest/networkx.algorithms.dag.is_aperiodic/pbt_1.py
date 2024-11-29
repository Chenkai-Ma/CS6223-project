from hypothesis import given, strategies as st
import networkx as nx

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, unique=True))
def test_is_aperiodic_acylc_graph_property(edges):
    DG = nx.DiGraph(edges)
    if not nx.is_directed(DG):
        return  # Skip if the graph is not directed
    if len(DG) == 0 or nx.is_empty(DG):
        return  # Skip if the graph is empty
    assert nx.is_aperiodic(DG) is False  # Acyclic graphs should not be aperiodic

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, unique=True))
def test_is_aperiodic_single_cycle_property(edges):
    if not edges:
        return  # Skip if there are no edges
    DG = nx.DiGraph(edges)
    if len(DG) == 2 and edges[0][0] == edges[1][1]:  # A simple cycle of length 2
        assert nx.is_aperiodic(DG) is False  # Should not be aperiodic

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, unique=True))
def test_is_aperiodic_coprime_cycles_property(edges):
    DG = nx.DiGraph(edges)
    if len(DG) == 0:
        return  # Skip if the graph is empty
    cycle_lengths = [2, 3]  # Example with coprime lengths
    if set(cycle_lengths).issubset(set(DG.nodes())):
        assert nx.is_aperiodic(DG) is True  # Should be aperiodic

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, unique=True))
def test_is_aperiodic_empty_graph_property(edges):
    DG = nx.DiGraph(edges)
    if len(DG) == 0:
        with pytest.raises(nx.NetworkXPointlessConcept):
            nx.is_aperiodic(DG)  # Must raise an error for empty graph

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, unique=True))
def test_is_aperiodic_dag_property(edges):
    DG = nx.DiGraph(edges)
    if nx.is_directed(DG) and not nx.has_path(DG, edges[0][0], edges[0][1]):
        assert nx.is_aperiodic(DG) is False  # Directed acyclic graphs should not be aperiodic
# End program