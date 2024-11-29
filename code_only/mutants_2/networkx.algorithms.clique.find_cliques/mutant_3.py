# property to violate: The function should yield all maximal cliques, meaning no additional nodes can be added to any returned clique without breaking its completeness.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_1():
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    # Deliberately adding an extra node to the cliques
    cliques.append([cliques[0][0], graph.nodes[0]])  # Add a node that is connected to the first clique
    for clique in cliques:
        # Check that no nodes can be added to the clique without breaking its completeness
        for node in graph.nodes:
            if node not in clique and graph.has_edges_from((node, n) for n in clique):
                assert False  # A node can be added to the clique

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_2():
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    # Remove a node from the first clique to allow for expansion
    if cliques:
        cliques[0].remove(cliques[0][0])  # Remove a node from the first clique
    for clique in cliques:
        # Check that no nodes can be added to the clique without breaking its completeness
        for node in graph.nodes:
            if node not in clique and graph.has_edges_from((node, n) for n in clique):
                assert False  # A node can be added to the clique

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_3():
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    # Intentionally duplicate a clique to create a violation
    if cliques:
        cliques.append(cliques[0])  # Duplicate the first clique
    for clique in cliques:
        # Check that no nodes can be added to the clique without breaking its completeness
        for node in graph.nodes:
            if node not in clique and graph.has_edges_from((node, n) for n in clique):
                assert False  # A node can be added to the clique

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_4():
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    # Add a non-adjacent node to the first clique to violate maximality
    if cliques:
        cliques[0].append(graph.nodes[-1])  # Add a node that is not connected to the first clique
    for clique in cliques:
        # Check that no nodes can be added to the clique without breaking its completeness
        for node in graph.nodes:
            if node not in clique and graph.has_edges_from((node, n) for n in clique):
                assert False  # A node can be added to the clique

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_5():
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    # Create a new clique that is not maximal by including a node that is not connected
    cliques.append([cliques[0][0], graph.nodes[0], graph.nodes[1]])  # Add unconnected nodes
    for clique in cliques:
        # Check that no nodes can be added to the clique without breaking its completeness
        for node in graph.nodes:
            if node not in clique and graph.has_edges_from((node, n) for n in clique):
                assert False  # A node can be added to the clique