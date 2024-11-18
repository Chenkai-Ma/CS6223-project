# property to violate: For directed graphs, if the orientation is set to 'original', the output edges must respect the original direction of the edges in the graph.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXNoCycle

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_violation_of_networkx_algorithms_cycles_find_cycle_1(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        for u, v, direction in cycle:
            assert (v, u) in G.edges()  # Edges must not respect the original direction.
    except NetworkXNoCycle:
        pass  # No cycle found is valid.

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_violation_of_networkx_algorithms_cycles_find_cycle_2(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        for u, v, direction in cycle:
            assert (u, v) not in G.edges()  # Edges must not respect the original direction.
    except NetworkXNoCycle:
        pass  # No cycle found is valid.

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_violation_of_networkx_algorithms_cycles_find_cycle_3(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        for u, v, direction in cycle:
            assert (u, v) in G.edges() or (v, u) in G.edges()  # Edges must not respect the original direction.
    except NetworkXNoCycle:
        pass  # No cycle found is valid.

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_violation_of_networkx_algorithms_cycles_find_cycle_4(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        for u, v, direction in cycle:
            assert (u, v) in G.edges() and (v, u) in G.edges()  # Edges must not respect the original direction.
    except NetworkXNoCycle:
        pass  # No cycle found is valid.

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_violation_of_networkx_algorithms_cycles_find_cycle_5(edges):
    G = nx.DiGraph(edges)
    try:
        cycle = nx.find_cycle(G, orientation='original')
        for u, v, direction in cycle:
            assert (u, v) in G.edges() and (u, v) not in G.edges()  # Edges must not respect the original direction.
    except NetworkXNoCycle:
        pass  # No cycle found is valid.