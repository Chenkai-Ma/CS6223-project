from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXNoCycle

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_cycle_not_empty_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G)
        assert len(cycle) > 0  # Cycle must have at least one edge
    except NetworkXNoCycle:
        pass  # If no cycle, we do not assert anything

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_cycle_valid_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G)
        # The last node of the last edge must connect back to the first node of the first edge
        assert cycle[0][0] == cycle[-1][1]
    except NetworkXNoCycle:
        pass  # If no cycle, we do not assert anything

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_cycle_original_orientation_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        for u, v in cycle:
            assert (u, v) in G.edges()  # Edges must respect original direction
    except NetworkXNoCycle:
        pass  # If no cycle, we do not assert anything

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_cycle_ignore_orientation_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='ignore')
        # The edges are treated as undirected, so we check both directions
        for u, v in cycle:
            assert (u, v) in G.edges() or (v, u) in G.edges()  # Edges must not respect direction
    except NetworkXNoCycle:
        pass  # If no cycle, we do not assert anything

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_cycle_directional_info_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        for edge in cycle:
            assert len(edge) == 3  # Each edge must include direction info when orientation is specified
    except NetworkXNoCycle:
        pass  # If no cycle, we do not assert anything
# End program