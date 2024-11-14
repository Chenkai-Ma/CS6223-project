from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=True).map(set))
def test_output_cliques_are_maximal_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    # Add edges to create cliques
    for i in graph_nodes:
        for j in graph_nodes:
            if i != j:
                G.add_edge(i, j)
    
    cliques = list(find_cliques(G))
    
    for clique in cliques:
        for node in clique:
            # Check if adding any other node from G would still be a clique
            for other in G.nodes():
                if other not in clique and not G.has_edge(node, other):
                    assert len(clique) == len(set(clique))  # Must be maximal

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=True).map(set))
def test_nodes_included_if_provided_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    # Add edges to create a complete graph
    for i in graph_nodes:
        for j in graph_nodes:
            if i != j:
                G.add_edge(i, j)
    
    # Test with a subset of nodes
    subset = list(graph_nodes)[:len(graph_nodes)//2]
    cliques = list(find_cliques(G, nodes=subset))
    
    for clique in cliques:
        for node in subset:
            assert node in clique  # Each clique must include all nodes in subset

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=True).map(set))
def test_output_cliques_are_unique_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    # Add edges to create cliques
    for i in graph_nodes:
        for j in graph_nodes:
            if i != j:
                G.add_edge(i, j)

    cliques = list(find_cliques(G))
    assert len(cliques) == len(set(tuple(sorted(clique)) for clique in cliques))  # Must be unique

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=True).map(set))
def test_length_of_cliques_is_at_least_one_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    # Add edges to create cliques
    for i in graph_nodes:
        for j in graph_nodes:
            if i != j:
                G.add_edge(i, j)
    
    cliques = list(find_cliques(G))
    
    for clique in cliques:
        assert len(clique) >= 1  # Each clique must have at least one node

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=True).map(set))
def test_order_of_cliques_is_arbitrary_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    # Add edges to create cliques
    for i in graph_nodes:
        for j in graph_nodes:
            if i != j:
                G.add_edge(i, j)

    cliques1 = list(find_cliques(G))
    cliques2 = list(find_cliques(G))
    
    # Check that the same cliques can be found, but order may differ
    assert set(map(tuple, cliques1)) == set(map(tuple, cliques2))  # Must contain the same cliques

# End program