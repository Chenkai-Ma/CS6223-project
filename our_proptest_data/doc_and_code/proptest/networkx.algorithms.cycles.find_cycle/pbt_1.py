from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXNoCycle

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True, min_size=1))
def test_cycle_found_property(edges):
    G = nx.Graph(edges)
    cycle = nx.find_cycle(G, orientation='ignore')
    assert len(cycle) > 0  # A cycle must be found.

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True, min_size=1))
def test_cycle_closed_loop_property(edges):
    G = nx.Graph(edges)
    cycle = nx.find_cycle(G, orientation='ignore')
    # Extract the tail of the first edge and head of the last edge
    first_edge = cycle[0]
    last_edge = cycle[-1]
    assert first_edge[0] == last_edge[1]  # Last edge must connect back to the first edge.

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True, min_size=1))
def test_orientation_respected_property(edges):
    G = nx.DiGraph(edges)
    cycle_original = nx.find_cycle(G, orientation='original')
    cycle_reverse = nx.find_cycle(G, orientation='reverse')
    # Check that the traversal direction is respected
    for edge in cycle_original:
        assert edge in G.edges()  # Must respect original orientation
    for edge in cycle_reverse:
        assert (edge[1], edge[0]) in G.edges()  # Must respect reverse orientation

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True, min_size=1))
def test_no_cycle_in_acyclic_graph_property(edges):
    G = nx.DiGraph(edges)
    if not nx.is_directed_acyclic_graph(G):
        return  # Skip if the graph is not acyclic
    try:
        nx.find_cycle(G)
        assert False  # Should raise an exception
    except NetworkXNoCycle:
        assert True  # Exception raised as expected

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True, min_size=1))
def test_edges_ordered_correctly_property(edges):
    G = nx.Graph(edges)
    cycle = nx.find_cycle(G, orientation='ignore')
    # Check if the edges in the cycle are in the order they were traversed
    assert all(cycle[i][1] == cycle[i + 1][0] for i in range(len(cycle) - 1))  # Edge order must be correct
# End program