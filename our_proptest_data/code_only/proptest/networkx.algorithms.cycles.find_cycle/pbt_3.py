from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_cycle_edges_form_closed_loop_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1)),
        st.builds(nx.DiGraph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
    ))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.sampled_from([None, "original", "reverse", "ignore"]))
    
    cycle = nx.algorithms.cycles.find_cycle(G, source=source, orientation=orientation)
    
    if cycle:
        tail, head = cycle[0]
        assert head in (e[0] for e in cycle[1:]), "Cycle does not close."

@given(st.data())
def test_no_cycle_in_acyclic_graph_property(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1, unique=True)))
    G = nx.dag.transitive_closure(G)  # Ensure it's acyclic
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.sampled_from([None, "original", "reverse", "ignore"]))
    
    cycle = nx.algorithms.cycles.find_cycle(G, source=source, orientation=orientation)
    
    assert cycle == [], "Expected an empty cycle for an acyclic graph."

@given(st.data())
def test_cycle_length_property(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()), min_size=3)))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.sampled_from([None, "original", "reverse", "ignore"]))
    
    cycle = nx.algorithms.cycles.find_cycle(G, source=source, orientation=orientation)
    
    if cycle:
        assert len(cycle) >= 3, "Cycle must have at least 3 edges."

@given(st.data())
def test_cycle_edges_exist_in_graph_property(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.sampled_from([None, "original", "reverse", "ignore"]))
    
    cycle = nx.algorithms.cycles.find_cycle(G, source=source, orientation=orientation)
    
    if cycle:
        for edge in cycle:
            assert edge in G.edges, "Cycle contains an edge not in the original graph."

@given(st.data())
def test_reverse_orientation_cycle_property(data):
    G = data.draw(st.builds(nx.DiGraph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = "reverse"
    
    cycle = nx.algorithms.cycles.find_cycle(G, source=source, orientation=orientation)
    
    if cycle:
        for edge in cycle:
            assert edge[::-1] in G.edges, "The reverse cycle does not correspond to the edges in the original graph."
# End program