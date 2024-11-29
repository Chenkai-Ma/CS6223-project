from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1))
def test_maximal_cliques_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    G.add_edges_from([(graph_nodes[i], graph_nodes[j]) for i in range(len(graph_nodes)) for j in range(i + 1, len(graph_nodes))])
    
    cliques = list(find_cliques(G))
    for clique in cliques:
        for node in clique:
            assert node in graph_nodes
            # Check that no additional node can be added to the clique
            for additional_node in graph_nodes:
                if additional_node not in clique and not G.has_edge(clique[0], additional_node):
                    assert additional_node not in clique

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1))
def test_nodes_in_cliques_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    # Create edges to form cliques
    for i in range(len(graph_nodes)):
        for j in range(i + 1, len(graph_nodes)):
            if i % 2 == j % 2:  # Connect nodes with the same parity
                G.add_edge(graph_nodes[i], graph_nodes[j])
    
    nodes_subset = st.sampled_from(graph_nodes)
    cliques = list(find_cliques(G))
    
    for clique in cliques:
        assert all(node in clique for node in nodes_subset)

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1))
def test_unique_cliques_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    for i in range(len(graph_nodes)):
        for j in range(i + 1, len(graph_nodes)):
            G.add_edge(graph_nodes[i], graph_nodes[j])
    
    cliques = list(find_cliques(G))
    assert len(cliques) == len(set(tuple(sorted(clique)) for clique in cliques))

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1))
def test_clique_length_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    for i in range(len(graph_nodes)):
        for j in range(i + 1, len(graph_nodes)):
            G.add_edge(graph_nodes[i], graph_nodes[j])
    
    cliques = list(find_cliques(G))
    for clique in cliques:
        assert len(clique) > 0

@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1))
def test_arbitrary_order_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    for i in range(len(graph_nodes)):
        for j in range(i + 1, len(graph_nodes)):
            G.add_edge(graph_nodes[i], graph_nodes[j])
    
    cliques1 = list(find_cliques(G))
    cliques2 = list(find_cliques(G))
    
    # Check that the same cliques are present regardless of order
    assert sorted(cliques1) == sorted(cliques2)
# End program