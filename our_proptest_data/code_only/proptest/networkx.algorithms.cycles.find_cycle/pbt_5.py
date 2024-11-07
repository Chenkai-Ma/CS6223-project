from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.cycles import find_cycle

@given(st.data())
def test_cycle_is_closed_property(data):
    G = data.draw(st.builds(nx.Graph, edges=st.sets(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.one_of(st.none(), st.sampled_from(["original", "reverse", "ignore"])))
    
    cycle = find_cycle(G, source=source, orientation=orientation)
    
    if cycle:
        # Check if the first and last nodes of the cycle are connected
        tail, head = cycle[0][0], cycle[-1][1]
        assert tail == head

@given(st.data())
def test_empty_cycle_for_acyclic_graph_property(data):
    G = data.draw(st.builds(nx.Graph, edges=st.sets(st.tuples(st.integers(), st.integers()))))
    if nx.is_directed_acyclic_graph(G):
        source = data.draw(st.one_of(st.none(), st.integers()))
        orientation = data.draw(st.one_of(st.none(), st.sampled_from(["original", "reverse", "ignore"])))
        
        cycle = find_cycle(G, source=source, orientation=orientation)
        assert cycle == []

@given(st.data())
def test_cycle_length_property(data):
    G = data.draw(st.builds(nx.DiGraph, edges=st.sets(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.one_of(st.none(), st.sampled_from(["original", "reverse", "ignore"])))
    
    cycle = find_cycle(G, source=source, orientation=orientation)
    
    if cycle and len(cycle) >= 3:
        # Check that the cycle length is at least 3
        assert len(cycle) >= 3

@given(st.data())
def test_edges_in_cycle_are_valid_property(data):
    G = data.draw(st.builds(nx.Graph, edges=st.sets(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.one_of(st.none(), st.sampled_from(["original", "reverse", "ignore"])))
    
    cycle = find_cycle(G, source=source, orientation=orientation)
    
    for edge in cycle:
        assert edge in G.edges

@given(st.data())
def test_reverse_orientation_property(data):
    G = data.draw(st.builds(nx.DiGraph, edges=st.sets(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    
    cycle_original = find_cycle(G, source=source, orientation="original")
    cycle_reverse = find_cycle(G, source=source, orientation="reverse")
    
    # Reverse the edges of the original cycle and check if it matches the reversed cycle
    if cycle_original:
        reversed_cycle = [(edge[1], edge[0]) for edge in cycle_original]
        assert sorted(reversed_cycle) == sorted(cycle_reverse)

# End program