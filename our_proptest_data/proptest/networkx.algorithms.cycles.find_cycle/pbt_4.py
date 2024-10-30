from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXNoCycle

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=50).distinct())
def test_find_cycle_edges_property(edges):
    G = nx.Graph(edges)
    if nx.is_empty_graph(G):
        return  # Skip empty graph
    try:
        cycle = nx.find_cycle(G)
        assert len(cycle) >= 1  # There must be at least one edge in the cycle
    except NetworkXNoCycle:
        pass  # No cycle found, which is acceptable

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=50).distinct())
def test_find_cycle_valid_cycle_property(edges):
    G = nx.Graph(edges)
    if nx.is_empty_graph(G):
        return  # Skip empty graph
    try:
        cycle = nx.find_cycle(G)
        # Check if the last node of the last edge connects back to the first node of the first edge
        assert cycle[0][0] == cycle[-1][1]  # The cycle must be valid
    except NetworkXNoCycle:
        pass  # No cycle found, which is acceptable

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=50).distinct())
def test_find_cycle_original_orientation_property(edges):
    G = nx.DiGraph(edges)
    if nx.is_empty_graph(G):
        return  # Skip empty graph
    try:
        cycle = nx.find_cycle(G, orientation='original')
        # Check that all edges respect the original direction
        for u, v in cycle:
            assert (u, v) in G.edges()  # Edge must exist in the original orientation
    except NetworkXNoCycle:
        pass  # No cycle found, which is acceptable

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=50).distinct())
def test_find_cycle_ignore_orientation_property(edges):
    G = nx.DiGraph(edges)
    if nx.is_empty_graph(G):
        return  # Skip empty graph
    try:
        cycle = nx.find_cycle(G, orientation='ignore')
        # Check that edges in the cycle can be traversed in any direction
        for u, v in cycle:
            assert (u, v) in G.edges() or (v, u) in G.edges()  # Either direction must exist
    except NetworkXNoCycle:
        pass  # No cycle found, which is acceptable

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=50).distinct())
def test_find_cycle_directional_info_property(edges):
    G = nx.DiGraph(edges)
    if nx.is_empty_graph(G):
        return  # Skip empty graph
    try:
        cycle = nx.find_cycle(G, orientation='original')
        # Check that each edge includes directional information
        for edge in cycle:
            assert len(edge) == 3  # Each edge should be of the form (u, v, direction)
            assert edge[2] in ('forward', 'reverse')  # Direction must be either 'forward' or 'reverse'
    except NetworkXNoCycle:
        pass  # No cycle found, which is acceptable
# End program