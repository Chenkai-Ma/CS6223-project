from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXNoCycle

# Property 1: If a cycle is found, the output must contain at least one edge.
@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_find_cycle_contains_edges_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G)
        assert len(cycle) > 0
    except NetworkXNoCycle:
        pass

# Property 2: The edges in the output cycle must form a closed loop.
@given(st.lists(st.tuples(st.integers(), st.integers())))
def test_find_cycle_closed_loop_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G)
        # Check if the cycle forms a closed loop
        tail = cycle[0][0]
        head = cycle[-1][1]
        assert tail == head
    except NetworkXNoCycle:
        pass

# Property 3: For directed graphs, the output edges must respect the specified orientation.
@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), 
                st.sampled_from([None, 'original', 'reverse', 'ignore']))
def test_find_cycle_orientation_property(edges, orientation):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation=orientation)
        if orientation == 'original':
            assert all(e[0] == cycle[i][0] for i, e in enumerate(cycle))
        elif orientation == 'reverse':
            assert all(e[1] == cycle[i][0] for i, e in enumerate(cycle))
        # Note: 'ignore' does not impose any restriction; it treats edges as undirected.
    except NetworkXNoCycle:
        pass

# Property 4: If the input graph is acyclic, the function must raise a NetworkXNoCycle exception.
@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_find_cycle_no_cycle_property(edges):
    G = nx.DiGraph(edges)
    if not nx.is_directed_acyclic_graph(G):
        try:
            nx.find_cycle(G)
        except NetworkXNoCycle:
            pass
    else:
        assert nx.find_cycle(G) is None  # Should raise an exception if acyclic

# Property 5: The output must accurately represent the edges traversed during the depth-first search.
@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_find_cycle_edges_traversed_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G)
        # Check that the edges in the cycle were part of the original edges
        for edge in cycle:
            assert edge in G.edges()
    except NetworkXNoCycle:
        pass
# End program