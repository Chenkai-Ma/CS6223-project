from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXNoCycle

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), 
               st.sampled_from(['original', 'reverse', 'ignore', None]))
def test_find_cycle_non_empty_cycle_property(edges, orientation):
    G = nx.Graph(edges)
    try:
        cycle = nx.find_cycle(G, orientation=orientation)
        assert len(cycle) > 0  # There should be at least one edge if a cycle is found.
    except NetworkXNoCycle:
        pass  # No cycle found is valid.

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), 
               st.sampled_from(['original', 'reverse', 'ignore', None]))
def test_find_cycle_valid_cycle_property(edges, orientation):
    G = nx.Graph(edges)
    try:
        cycle = nx.find_cycle(G, orientation=orientation)
        # Check if the last node of the last edge connects back to the first node of the first edge.
        assert cycle[0][0] == cycle[-1][1]
    except NetworkXNoCycle:
        pass  # No cycle found is valid.

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_find_cycle_original_orientation_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        for u, v, direction in cycle:
            assert (u, v) in G.edges()  # Edges must respect the original direction.
    except NetworkXNoCycle:
        pass  # No cycle found is valid.

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_find_cycle_ignore_orientation_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='ignore')
        for u, v, direction in cycle:
            assert (u, v) in G.edges() or (v, u) in G.edges()  # Edges must be treated as undirected.
    except NetworkXNoCycle:
        pass  # No cycle found is valid.

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), 
               st.sampled_from(['original', 'reverse', 'ignore']))
def test_find_cycle_directional_information_property(edges, orientation):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation=orientation)
        for u, v, direction in cycle:
            assert direction in ['forward', 'reverse']  # Direction must be recorded if orientation is specified.
    except NetworkXNoCycle:
        pass  # No cycle found is valid.
# End program