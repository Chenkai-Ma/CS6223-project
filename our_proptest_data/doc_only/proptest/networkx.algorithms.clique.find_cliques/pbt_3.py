from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.data())
def test_find_cliques_subsets_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(G))
    for clique in cliques:
        assert all(node in G.nodes for node in clique)

@given(st.data())
def test_find_cliques_non_empty_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(G))
    if G.nodes:
        assert all(len(clique) > 0 for clique in cliques)

@given(st.data())
def test_find_cliques_maximal_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(G))
    for clique in cliques:
        for node in G.nodes:
            if node not in clique and all(neighbor in clique for neighbor in G.neighbors(node)):
                assert False  # If we can add a node without breaking the clique property

@given(st.data())
def test_find_cliques_include_nodes_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=100)))
    nodes = data.draw(st.lists(st.sampled_from(G.nodes), min_size=1, max_size=5))
    if nx.is_clique(G, nodes):
        cliques = list(find_cliques(G, nodes=nodes))
        assert all(all(node in clique for node in nodes) for clique in cliques)

@given(st.data())
def test_find_cliques_unique_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(G))
    assert len(cliques) == len(set(map(tuple, cliques)))  # Check for uniqueness of cliques
# End program