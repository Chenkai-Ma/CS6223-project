from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXNoCycle

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), 
                st.integers())
def test_cycle_found_property(edges, source):
    G = nx.Graph(edges)
    cycle = nx.find_cycle(G, source=source)
    assert len(cycle) > 0  # Output must contain at least one edge if a cycle is found.

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), 
                st.integers())
def test_cycle_closed_loop_property(edges, source):
    G = nx.Graph(edges)
    try:
        cycle = nx.find_cycle(G, source=source)
        tail = cycle[-1][0]
        head = cycle[0][1]
        assert tail == head  # The last edge must connect back to the first edge.
    except NetworkXNoCycle:
        pass  # If no cycle, the property holds trivially.

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), 
                st.one_of(st.just('original'), st.just('reverse'), st.just('ignore')))
def test_orientation_respected_property(edges, orientation):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation=orientation)
        for edge in cycle:
            if orientation == 'original':
                assert (edge[0], edge[1]) in G.edges()
            elif orientation == 'reverse':
                assert (edge[1], edge[0]) in G.edges()
            elif orientation == 'ignore':
                assert (edge[0], edge[1]) in G.edges() or (edge[1], edge[0]) in G.edges()
    except NetworkXNoCycle:
        pass  # No cycle found, property holds trivially.

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_no_cycle_in_acyclic_graph_property(edges):
    G = nx.DiGraph(edges)
    # Ensure the graph is acyclic by checking its DAG property
    if nx.is_directed_acyclic_graph(G):
        try:
            nx.find_cycle(G)  # Should raise an exception
            assert False  # If we reach here, the test fails
        except NetworkXNoCycle:
            assert True  # Correct behavior, exception raised
    else:
        try:
            cycle = nx.find_cycle(G)  # May or may not find a cycle
            assert len(cycle) > 0  # If a cycle is found, it should not be empty
        except NetworkXNoCycle:
            pass  # If no cycle, property holds trivially.

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), 
                st.integers())
def test_edges_in_traversal_order_property(edges, source):
    G = nx.Graph(edges)
    try:
        cycle = nx.find_cycle(G, source=source)
        cycle_edges = [edge[:2] for edge in cycle]  # Get only the tail and head
        assert cycle_edges == list(dict.fromkeys(cycle_edges))  # Ensure edges are in the order of traversal
    except NetworkXNoCycle:
        pass  # No cycle found, property holds trivially.
# End program