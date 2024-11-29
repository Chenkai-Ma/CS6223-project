from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_nodes_are_in_input_graph_property(data):
    # Generate a graph and nodes for testing
    G = nx.generators.random_graphs.gnp_random_graph(10, 0.5)
    nodes = list(G.nodes())
    
    # Call the find_cliques function
    cliques = list(nx.algorithms.clique.find_cliques(G))
    
    # Check that all nodes in the cliques are in the original graph
    for clique in cliques:
        assert all(node in G.nodes() for node in clique)

@given(st.data())
def test_cliques_are_complete_subgraphs_property(data):
    # Generate a graph for testing
    G = nx.generators.random_graphs.gnp_random_graph(10, 0.5)
    
    # Call the find_cliques function
    cliques = list(nx.algorithms.clique.find_cliques(G))
    
    # Check that each clique is a complete subgraph
    for clique in cliques:
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                assert G.has_edge(clique[i], clique[j])

@given(st.data())
def test_yields_all_maximal_cliques_property(data):
    # Generate a graph for testing
    G = nx.generators.random_graphs.gnp_random_graph(10, 0.5)
    
    # Call the find_cliques function
    cliques = list(nx.algorithms.clique.find_cliques(G))
    
    # Check that no additional nodes can be added to the cliques
    for clique in cliques:
        for node in G.nodes():
            if node not in clique:
                assert not all(G.has_edge(node, other) for other in clique)

@given(st.data())
def test_empty_graph_yields_no_cliques_property(data):
    # Create an empty graph
    G = nx.Graph()
    
    # Call the find_cliques function
    cliques = list(nx.algorithms.clique.find_cliques(G))
    
    # Check that no cliques are yielded
    assert cliques == []

@given(st.data())
def test_specific_nodes_form_clique_or_raise_property(data):
    # Generate a random graph and select nodes
    G = nx.generators.random_graphs.gnp_random_graph(10, 0.5)
    nodes = list(G.nodes())
    
    # Test with a subset of nodes
    if len(nodes) > 1:
        sub_nodes = nodes[:2]
        if all(G.has_edge(sub_nodes[i], sub_nodes[j]) for i in range(len(sub_nodes)) for j in range(i + 1, len(sub_nodes))):
            # Should not raise an error
            try:
                cliques = list(nx.algorithms.clique.find_cliques(G, nodes=sub_nodes))
                assert any(set(sub_nodes) == set(clique) for clique in cliques)
            except ValueError:
                assert False  # Should not raise
        else:
            # Should raise an error
            with pytest.raises(ValueError):
                list(nx.algorithms.clique.find_cliques(G, nodes=sub_nodes))

# End program