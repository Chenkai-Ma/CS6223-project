# property to violate: If the input graph is empty, the function should yield no cliques, returning an empty output.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_1():
    graph = nx.Graph()
    cliques = list(find_cliques(graph))
    assert cliques == [[0]]  # Violating the property by asserting a non-empty list.

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_2():
    graph = nx.Graph()
    cliques = list(find_cliques(graph))
    assert cliques == [None]  # Violating the property by asserting a list containing None.

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_3():
    graph = nx.Graph()
    cliques = list(find_cliques(graph))
    assert cliques == [[1, 2]]  # Violating the property by asserting a non-empty list with arbitrary nodes.

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_4():
    graph = nx.Graph()
    cliques = list(find_cliques(graph))
    assert cliques == [[], []]  # Violating the property by asserting a list containing empty lists.

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_5():
    graph = nx.Graph()
    cliques = list(find_cliques(graph))
    assert cliques == [[0, 1, 2]]  # Violating the property by asserting a non-empty list with multiple nodes.