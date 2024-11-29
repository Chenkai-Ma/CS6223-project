# property to violate: Each returned clique must be a complete subgraph, meaning that every pair of nodes within the clique must be directly connected by an edge in the graph.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_1(data):
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    # Introduce a non-edge between the first two nodes of the first clique
    if cliques:
        clique = cliques[0]
        if len(clique) > 1:
            graph.remove_edge(clique[0], clique[1])
    for clique in cliques:
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                assert graph.has_edge(clique[i], clique[j])

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_2(data):
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    # Remove an edge between the last two nodes of the first clique
    if cliques:
        clique = cliques[0]
        if len(clique) > 1:
            graph.remove_edge(clique[-1], clique[-2])
    for clique in cliques:
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                assert graph.has_edge(clique[i], clique[j])

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_3(data):
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    # Remove an edge between two arbitrary nodes in the first clique
    if cliques:
        clique = cliques[0]
        if len(clique) > 2:
            graph.remove_edge(clique[0], clique[2])
    for clique in cliques:
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                assert graph.has_edge(clique[i], clique[j])

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_4(data):
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    # Remove an edge between the first two nodes of the last clique
    if cliques:
        clique = cliques[-1]
        if len(clique) > 1:
            graph.remove_edge(clique[0], clique[1])
    for clique in cliques:
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                assert graph.has_edge(clique[i], clique[j])

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_5(data):
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    # Remove an edge between two random nodes in the first clique
    if cliques:
        clique = cliques[0]
        if len(clique) > 2:
            graph.remove_edge(clique[1], clique[2])
    for clique in cliques:
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                assert graph.has_edge(clique[i], clique[j])