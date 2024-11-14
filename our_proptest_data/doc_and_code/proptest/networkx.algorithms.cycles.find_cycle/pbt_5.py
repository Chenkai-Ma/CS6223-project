from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXNoCycle

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=50).distinct())
def test_cycle_found_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G)
        assert len(cycle) > 0  # If a cycle is found, it must contain at least one edge
    except NetworkXNoCycle:
        pass  # No cycle found, which is expected for acyclic graphs

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=50).distinct())
def test_cycle_closed_loop_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G)
        if len(cycle) > 0:
            assert cycle[0][0] == cycle[-1][1]  # The head of the last edge must connect back to the tail of the first edge
    except NetworkXNoCycle:
        pass  # No cycle found, which is expected for acyclic graphs

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=50).distinct(), st.sampled_from(['original', 'reverse', 'ignore']))
def test_orientation_respected_property(edges, orientation):
    G = nx.DiGraph(edges)
    cycle = nx.find_cycle(G, orientation=orientation)
    if len(cycle) > 0:
        for edge in cycle:
            if orientation == 'original':
                assert edge[0] in G.predecessors(edge[1])  # Follow original direction
            elif orientation == 'reverse':
                assert edge[1] in G.predecessors(edge[0])  # Follow reversed direction

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=50).distinct())
def test_no_cycle_exception_property(edges):
    G = nx.DiGraph(edges)
    if not nx.is_directed_acyclic_graph(G):
        try:
            nx.find_cycle(G)
            assert False  # Should raise an exception if a cycle exists
        except NetworkXNoCycle:
            pass  # This is expected for acyclic graphs

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=50).distinct())
def test_edges_order_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G)
        if len(cycle) > 0:
            for i in range(len(cycle) - 1):
                assert cycle[i][1] == cycle[i + 1][0]  # Ensure that edges are traversed in the correct order
    except NetworkXNoCycle:
        pass  # No cycle found, which is expected for acyclic graphs
# End program