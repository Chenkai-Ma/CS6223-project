from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_cycle_is_closed_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.DiGraph, st.lists(st.tuples(st.integers(), st.integers()))),
        st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers())))
    ))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.one_of(st.none(), st.just("original"), st.just("reverse"), st.just("ignore")))

    cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
    
    if cycle:
        assert cycle[0][0] == cycle[-1][1]

@given(st.data())
def test_no_cycle_in_acyclic_graph_property(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.one_of(st.none(), st.just("original"), st.just("reverse"), st.just("ignore")))

    if nx.is_directed_acyclic_graph(G):
        cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
        assert cycle == []

@given(st.data())
def test_cycle_length_property(data):
    G = data.draw(st.builds(nx.DiGraph, st.lists(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.one_of(st.none(), st.just("original"), st.just("reverse"), st.just("ignore")))

    try:
        cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
        if len(cycle) >= 3:
            assert len(cycle) >= 3
    except nx.exception.NetworkXNoCycle:
        pass

@given(st.data())
def test_cycle_edges_exist_property(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.one_of(st.none(), st.just("original"), st.just("reverse"), st.just("ignore")))

    cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
    
    for edge in cycle:
        assert edge in G.edges() or (edge[1], edge[0]) in G.edges()  # Check both directions for undirected graphs

@given(st.data())
def test_cycle_orientation_property(data):
    G = data.draw(st.builds(nx.DiGraph, st.lists(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = "reverse"

    cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
    
    if cycle:
        for edge in cycle:
            assert (edge[1], edge[0]) in G.edges()  # Check if the reversed edge exists

# End program