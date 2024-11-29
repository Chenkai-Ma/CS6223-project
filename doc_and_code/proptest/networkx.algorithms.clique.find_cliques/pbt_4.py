from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.data())
def test_cliques_are_maximal_property(data):
    G = nx.gnm_random_graph(data.draw(st.integers(min_value=1, max_value=100)), 
                              data.draw(st.integers(min_value=1, max_value=100)))
    cliques = list(find_cliques(G))
    for clique in cliques:
        for node in clique:
            neighbors = set(G[node])
            assert all(neighbor in clique for neighbor in neighbors if neighbor in clique)

@given(st.data())
def test_nodes_in_cliques_property(data):
    G = nx.gnm_random_graph(data.draw(st.integers(min_value=1, max_value=100)), 
                              data.draw(st.integers(min_value=1, max_value=100)))
    nodes = data.draw(st.lists(st.integers(min_value=0, max_value=len(G.nodes)-1), min_size=1, max_size=5))
                      if len(G.nodes) > 0 else st.lists(st.integers()))
    if all(n in G.nodes for n in nodes) and len(nodes) > 1:
        cliques = list(find_cliques(G, nodes))
        for clique in cliques:
            assert all(n in clique for n in nodes)
    else:
        try:
            list(find_cliques(G, nodes))
        except ValueError:
            pass

@given(st.data())
def test_unique_cliques_property(data):
    G = nx.gnm_random_graph(data.draw(st.integers(min_value=1, max_value=100)), 
                              data.draw(st.integers(min_value=1, max_value=100)))
    cliques = list(find_cliques(G))
    assert len(cliques) == len(set(tuple(sorted(clique)) for clique in cliques))

@given(st.data())
def test_clique_length_property(data):
    G = nx.gnm_random_graph(data.draw(st.integers(min_value=1, max_value=100)), 
                              data.draw(st.integers(min_value=1, max_value=100)))
    cliques = list(find_cliques(G))
    for clique in cliques:
        assert len(clique) >= 1

@given(st.data())
def test_arbitrary_order_property(data):
    G = nx.gnm_random_graph(data.draw(st.integers(min_value=1, max_value=100)), 
                              data.draw(st.integers(min_value=1, max_value=100)))
    cliques1 = list(find_cliques(G))
    cliques2 = list(find_cliques(G))
    assert set(tuple(sorted(clique)) for clique in cliques1) == set(tuple(sorted(clique)) for clique in cliques2)

# End program