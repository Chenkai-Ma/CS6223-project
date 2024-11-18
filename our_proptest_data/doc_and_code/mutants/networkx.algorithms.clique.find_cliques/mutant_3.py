# property to violate: The output should not include any duplicate cliques, ensuring that each maximal clique is unique within the iterator.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=True).map(set))
def test_violation_of_networkx_algorithms_clique_find_cliques_1(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    # Add edges to create cliques
    for i in graph_nodes:
        for j in graph_nodes:
            if i != j:
                G.add_edge(i, j)

    cliques = list(find_cliques(G))
    cliques.append(cliques[0])  # Introduce a duplicate of the first clique
    assert len(cliques) == len(set(tuple(sorted(clique)) for clique in cliques))  # Must be unique

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=True).map(set))
def test_violation_of_networkx_algorithms_clique_find_cliques_2(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    # Add edges to create cliques
    for i in graph_nodes:
        for j in graph_nodes:
            if i != j:
                G.add_edge(i, j)

    cliques = list(find_cliques(G))
    cliques.extend(cliques)  # Duplicate all cliques
    assert len(cliques) == len(set(tuple(sorted(clique)) for clique in cliques))  # Must be unique

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=True).map(set))
def test_violation_of_networkx_algorithms_clique_find_cliques_3(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    # Add edges to create cliques
    for i in graph_nodes:
        for j in graph_nodes:
            if i != j:
                G.add_edge(i, j)

    cliques = list(find_cliques(G))
    cliques += cliques[:2]  # Add the first two cliques again
    assert len(cliques) == len(set(tuple(sorted(clique)) for clique in cliques))  # Must be unique

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=True).map(set))
def test_violation_of_networkx_algorithms_clique_find_cliques_4(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    # Add edges to create cliques
    for i in graph_nodes:
        for j in graph_nodes:
            if i != j:
                G.add_edge(i, j)

    cliques = list(find_cliques(G))
    cliques.append(cliques[-1])  # Duplicate the last clique
    assert len(cliques) == len(set(tuple(sorted(clique)) for clique in cliques))  # Must be unique

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=True).map(set))
def test_violation_of_networkx_algorithms_clique_find_cliques_5(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    # Add edges to create cliques
    for i in graph_nodes:
        for j in graph_nodes:
            if i != j:
                G.add_edge(i, j)

    cliques = list(find_cliques(G))
    cliques += cliques[1:3]  # Duplicate a couple of cliques
    assert len(cliques) == len(set(tuple(sorted(clique)) for clique in cliques))  # Must be unique