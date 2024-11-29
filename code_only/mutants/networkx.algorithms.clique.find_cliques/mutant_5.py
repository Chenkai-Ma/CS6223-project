# property to violate: If specific nodes are provided as input, the function should only yield cliques that include those nodes, and it should raise an error if the provided nodes do not form a clique.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_1():
    nodes = data.draw(st.sets(st.integers(), min_size=2, max_size=10))
    graph = nx.complete_graph(nodes)  # Create a complete graph
    cliques = list(find_cliques(graph, nodes=list(nodes)))
    assert len(cliques) > 0  # There must be at least one clique, the nodes themselves
    for clique in cliques:
        assert set(clique) != set(nodes)  # Must not yield the specified clique

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_2():
    nodes = data.draw(st.sets(st.integers(), min_size=2, max_size=10))
    graph = nx.complete_graph(nodes)  # Create a complete graph
    cliques = list(find_cliques(graph, nodes=list(nodes)))
    assert len(cliques) > 0  # There must be at least one clique, the nodes themselves
    for clique in cliques:
        assert len(clique) > len(nodes)  # Must yield cliques larger than the specified nodes

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_3():
    nodes = data.draw(st.sets(st.integers(), min_size=2, max_size=10))
    graph = nx.complete_graph(nodes)  # Create a complete graph
    cliques = list(find_cliques(graph, nodes=list(nodes)))
    assert len(cliques) > 0  # There must be at least one clique, the nodes themselves
    for clique in cliques:
        assert set(nodes).issubset(set(clique))  # Must yield cliques that do not include the specified nodes

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_4():
    nodes = data.draw(st.sets(st.integers(), min_size=2, max_size=10))
    graph = nx.complete_graph(nodes)  # Create a complete graph
    cliques = list(find_cliques(graph, nodes=list(nodes)))
    assert len(cliques) > 0  # There must be at least one clique, the nodes themselves
    for clique in cliques:
        assert len(clique) < len(nodes)  # Must yield cliques smaller than the specified nodes

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_5():
    nodes = data.draw(st.sets(st.integers(), min_size=2, max_size=10))
    graph = nx.complete_graph(nodes)  # Create a complete graph
    cliques = list(find_cliques(graph, nodes=list(nodes)))
    assert len(cliques) > 0  # There must be at least one clique, the nodes themselves
    for clique in cliques:
        assert set(clique) != set(nodes) and len(clique) == len(nodes)  # Must yield cliques that are the same size but different