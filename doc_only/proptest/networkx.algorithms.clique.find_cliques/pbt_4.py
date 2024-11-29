from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.data())
def test_find_cliques_subsets_property(data):
    # Generate a random undirected graph
    G = nx.generators.random_graphs.gnp_random_graph(data.draw(st.integers(min_value=1, max_value=100)), 0.5)
    cliques = list(find_cliques(G))
    
    # Check that all cliques are subsets of nodes in G
    for clique in cliques:
        assert all(node in G.nodes for node in clique)

@given(st.data())
def test_find_cliques_non_empty_property(data):
    # Generate a random undirected graph
    G = nx.generators.random_graphs.gnp_random_graph(data.draw(st.integers(min_value=1, max_value=100)), 0.5)
    cliques = list(find_cliques(G))
    
    # Check that each clique contains at least one node if G is non-empty
    if G.number_of_nodes() > 0:
        assert all(len(clique) > 0 for clique in cliques)

@given(st.data())
def test_find_cliques_maximal_property(data):
    # Generate a random undirected graph
    G = nx.generators.random_graphs.gnp_random_graph(data.draw(st.integers(min_value=1, max_value=100)), 0.5)
    cliques = list(find_cliques(G))
    
    # Check that each clique is maximal
    for clique in cliques:
        for node in G.nodes:
            if node not in clique and all(neighbor in clique for neighbor in G.neighbors(node)):
                assert False  # Found a node that can be added to the clique, so it's not maximal

@given(st.data())
def test_find_cliques_includes_specified_nodes_property(data):
    # Generate a random undirected graph
    G = nx.generators.random_graphs.gnp_random_graph(data.draw(st.integers(min_value=1, max_value=100)), 0.5)
    nodes = data.draw(st.lists(st.sampled_from(G.nodes()), min_size=1, max_size=len(G.nodes())))
    
    if nx.is_clique(G.subgraph(nodes)):
        cliques = list(find_cliques(G, nodes=nodes))
        
        # Check that all returned cliques include the specified nodes
        for clique in cliques:
            assert all(node in clique for node in nodes)

@given(st.data())
def test_find_cliques_unique_cliques_property(data):
    # Generate a random undirected graph
    G = nx.generators.random_graphs.gnp_random_graph(data.draw(st.integers(min_value=1, max_value=100)), 0.5)
    cliques = list(find_cliques(G))
    
    # Check that there are no duplicate cliques
    unique_cliques = {tuple(sorted(clique)) for clique in cliques}
    assert len(unique_cliques) == len(cliques)
# End program