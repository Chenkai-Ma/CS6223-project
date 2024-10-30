from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXNoCycle

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True))
def test_cycle_found_property(edges):
    G = nx.Graph(edges)
    try:
        cycle = nx.find_cycle(G)
        assert len(cycle) > 0  # There must be at least one edge in the cycle
    except NetworkXNoCycle:
        pass  # If no cycle is found, we do nothing

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True))
def test_cycle_validity_property(edges):
    G = nx.Graph(edges)
    try:
        cycle = nx.find_cycle(G)
        # Extract the nodes in the cycle
        cycle_nodes = [u for u, v in cycle] + [cycle[-1][1]]  # Include last node to check cycle
        assert cycle_nodes[0] == cycle_nodes[-1]  # The first and last nodes must be the same
    except NetworkXNoCycle:
        pass  # If no cycle is found, we do nothing

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True))
def test_original_orientation_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        for (u, v) in cycle:
            assert (u, v) in G.edges()  # Edges must respect the original orientation
    except NetworkXNoCycle:
        pass  # If no cycle is found, we do nothing

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True))
def test_ignore_orientation_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='ignore')
        for (u, v) in cycle:
            assert (u, v) in G.edges() or (v, u) in G.edges()  # Edges must be treated as undirected
    except NetworkXNoCycle:
        pass  # If no cycle is found, we do nothing

@given(st.lists(st.tuples(st.integers(), st.integers()), unique=True))
def test_directional_info_property(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        for (u, v, direction) in cycle:
            assert direction in ['forward', 'reverse']  # Must include directional information
    except NetworkXNoCycle:
        pass  # If no cycle is found, we do nothing
# End program