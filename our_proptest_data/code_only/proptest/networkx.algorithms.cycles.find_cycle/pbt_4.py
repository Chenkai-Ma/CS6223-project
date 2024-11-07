from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_cycle_forms_closed_loop_property(data):
    G = data.draw(st.one_of(st.graphs()))
    source = data.draw(st.one_of([None, st.nodes(G)]))
    orientation = data.draw(st.sampled_from([None, "original", "reverse", "ignore"]))
    cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
    
    if cycle:
        first_edge = cycle[0]
        last_edge = cycle[-1]
        assert last_edge[1] == first_edge[0]  # last node connects back to the first node

@given(st.data())
def test_acyclic_graph_returns_empty_list_property(data):
    G = data.draw(st.graphs(directed=True, nodes=st.integers(min_value=0, max_value=100), edges=0))
    source = data.draw(st.one_of([None, st.nodes(G)]))
    orientation = data.draw(st.sampled_from([None, "original", "reverse", "ignore"]))
    cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
    
    assert cycle == []  # No cycle should be found

@given(st.data())
def test_found_cycle_has_minimum_length_property(data):
    G = data.draw(st.random_graphs())
    source = data.draw(st.one_of([None, st.nodes(G)]))
    orientation = data.draw(st.sampled_from([None, "original", "reverse", "ignore"]))
    cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
    
    if cycle:
        assert len(cycle) >= 3  # A cycle must have at least 3 edges

@given(st.data())
def test_cycle_edges_are_valid_edges_property(data):
    G = data.draw(st.random_graphs())
    source = data.draw(st.one_of([None, st.nodes(G)]))
    orientation = data.draw(st.sampled_from([None, "original", "reverse", "ignore"]))
    cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
    
    for edge in cycle:
        assert edge in G.edges()  # All edges in the cycle must be valid edges of the graph

@given(st.data())
def test_reverse_orientation_changes_cycle_direction_property(data):
    G = data.draw(st.random_graphs())
    source = data.draw(st.one_of([None, st.nodes(G)]))
    cycle_original = nx.algorithms.cycles.find_cycle(G, source, orientation=None)
    cycle_reverse = nx.algorithms.cycles.find_cycle(G, source, orientation="reverse")
    
    if cycle_original:
        assert len(cycle_original) == len(cycle_reverse)  # Both cycles should have the same length
        assert all(edge[::-1] in cycle_reverse for edge in cycle_original)  # Reverse of each edge must be in the reverse cycle

# End program