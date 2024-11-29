# property to violate: If the input graph is empty, the function should yield no cliques, returning an empty output.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_1(data):
    graph = nx.Graph()
    cliques = list(find_cliques(graph)) + [[0]]  # Adding a dummy clique
    assert cliques == []

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_2(data):
    graph = nx.Graph()
    cliques = list(find_cliques(graph)) + [[], []]  # Adding empty lists as cliques
    assert cliques == []

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_3(data):
    graph = nx.Graph()
    cliques = list(find_cliques(graph)) + [[1, 2]]  # Adding a non-existent clique
    assert cliques == []

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_4(data):
    graph = nx.Graph()
    cliques = list(find_cliques(graph)) + [[3]]  # Adding a single node as a clique
    assert cliques == []

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_5(data):
    graph = nx.Graph()
    cliques = list(find_cliques(graph)) + [[4, 5, 6]]  # Adding a non-existent larger clique
    assert cliques == []