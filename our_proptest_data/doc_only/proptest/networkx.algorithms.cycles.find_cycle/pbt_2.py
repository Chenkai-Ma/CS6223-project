from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXNoCycle

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True, min_size=1))
def test_cycle_found_property(edges):
    G = nx.Graph(edges)
    try:
        cycle = nx.find_cycle(G)
        assert len(cycle) > 0  # At least one edge should be present if a cycle is found.
    except NetworkXNoCycle:
        pass  # No cycle found, which is acceptable.

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True, min_size=1))
def test_cycle_validity_property(edges):
    G = nx.Graph(edges)
    try:
        cycle = nx.find_cycle(G)
        # Check that the last node of the last edge connects back to the first node of the first edge
        assert cycle[0][0] == cycle[-1][1]  # Last node must connect back to the first node.
    except NetworkXNoCycle:
        pass  # No cycle found, which is acceptable.

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True, min_size=1))
def test_cycle_original_orientation_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        for u, v, direction in cycle:
            # Ensure the edges respect the original direction
            assert (u, v) in G.edges()  # Edge must be in the original graph.
    except NetworkXNoCycle:
        pass  # No cycle found, which is acceptable.

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True, min_size=1))
def test_cycle_ignore_orientation_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='ignore')
        # Ignore original direction, but edges should still connect
        for i in range(len(cycle)):
            u, v, direction = cycle[i]
            # Check that the edge is treated as undirected
            assert (u, v) in G.edges() or (v, u) in G.edges()
    except NetworkXNoCycle:
        pass  # No cycle found, which is acceptable.

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True, min_size=1))
def test_cycle_directional_information_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='ignore')
        for u, v, direction in cycle:
            assert direction in ['forward', 'reverse']  # Directional information should be present.
    except NetworkXNoCycle:
        pass  # No cycle found, which is acceptable.
# End program