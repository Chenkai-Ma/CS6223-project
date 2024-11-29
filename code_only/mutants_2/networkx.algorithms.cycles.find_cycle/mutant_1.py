# property to violate: If the input graph is acyclic (i.e., it contains no cycles), the output should be an empty list.
from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_violation_of_networkx_algorithms_cycles_find_cycle_1(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.one_of(st.none(), st.just("original"), st.just("reverse"), st.just("ignore")))

    if nx.is_directed_acyclic_graph(G):
        cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
        assert cycle != []  # Violation: should be empty but is not.

@given(st.data())
def test_violation_of_networkx_algorithms_cycles_find_cycle_2(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.one_of(st.none(), st.just("original"), st.just("reverse"), st.just("ignore")))

    if nx.is_directed_acyclic_graph(G):
        cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
        assert cycle == [(0, 0)]  # Violation: returns a cycle instead of empty.

@given(st.data())
def test_violation_of_networkx_algorithms_cycles_find_cycle_3(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.one_of(st.none(), st.just("original"), st.just("reverse"), st.just("ignore")))

    if nx.is_directed_acyclic_graph(G):
        cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
        assert cycle == [(1, 2), (2, 3)]  # Violation: returns a non-empty cycle.

@given(st.data())
def test_violation_of_networkx_algorithms_cycles_find_cycle_4(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.one_of(st.none(), st.just("original"), st.just("reverse"), st.just("ignore")))

    if nx.is_directed_acyclic_graph(G):
        cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
        assert cycle == [(3, 4), (4, 5), (5, 3)]  # Violation: returns a cycle instead of empty.

@given(st.data())
def test_violation_of_networkx_algorithms_cycles_find_cycle_5(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()))))
    source = data.draw(st.one_of(st.none(), st.integers()))
    orientation = data.draw(st.one_of(st.none(), st.just("original"), st.just("reverse"), st.just("ignore")))

    if nx.is_directed_acyclic_graph(G):
        cycle = nx.algorithms.cycles.find_cycle(G, source, orientation)
        assert cycle == [(0, 1), (1, 2), (2, 0)]  # Violation: returns a cycle instead of empty.