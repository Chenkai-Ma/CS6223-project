from hypothesis import given, strategies as st
import networkx as nx
from hypothesis import example

@given(st.lists(st.integers(min_value=0, max_value=100), unique=True).map(nx.Graph.from_edges))
def test_find_cliques_maximal_property(G):
    cliques = list(nx.find_cliques(G))
    for clique in cliques:
        for node in clique:
            # Check if the clique is maximal
            assert all(node in G[n] for n in clique)  # must be a complete subgraph
            assert all(node not in G[n] for n in G if n not in clique)  # can't add any node

@given(st.lists(st.integers(min_value=0, max_value=100), unique=True).map(nx.Graph.from_edges),
               st.lists(st.integers(min_value=0, max_value=100), unique=True))
def test_find_cliques_nodes_property(G, nodes):
    if len(nodes) > 0:
        try:
            cliques = list(nx.find_cliques(G, nodes))
            for clique in cliques:
                assert all(node in clique for node in nodes)  # must contain all nodes
        except ValueError:
            # If nodes are not a clique, it's expected to raise ValueError
            pass

@given(st.lists(st.integers(min_value=0, max_value=100), unique=True).map(nx.Graph.from_edges))
def test_find_cliques_unique_cliques_property(G):
    cliques = list(nx.find_cliques(G))
    assert len(cliques) == len(set(map(tuple, cliques)))  # all cliques must be unique

@given(st.lists(st.integers(min_value=0, max_value=100), unique=True).map(nx.Graph.from_edges))
def test_find_cliques_non_empty_cliques_property(G):
    cliques = list(nx.find_cliques(G))
    for clique in cliques:
        assert len(clique) >= 1  # each clique must have at least one node

@given(st.lists(st.integers(min_value=0, max_value=100), unique=True).map(nx.Graph.from_edges))
def test_find_cliques_arbitrary_order_property(G):
    cliques_1 = list(nx.find_cliques(G))
    cliques_2 = list(nx.find_cliques(G))
    assert sorted(cliques_1) == sorted(cliques_2)  # the same cliques should be present regardless of order

# End program