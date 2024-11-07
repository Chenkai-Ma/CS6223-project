from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_nodes_subset_property(data):
    @st.composite
    def graphs(draw):
        nodes = draw(st.sets(st.integers(), min_size=1, max_size=100))
        edges = draw(st.sets(st.tuples(st.sampled_from(nodes), st.sampled_from(nodes)), min_size=0, max_size=1000))
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        return G, nodes

    G, nodes = graphs(data)
    cliques = list(nx.algorithms.clique.find_cliques(G))
    
    for clique in cliques:
        assert all(node in G.nodes for node in clique)

@given(st.data())
def test_cliques_complete_subgraph_property(data):
    @st.composite
    def graphs(draw):
        nodes = draw(st.sets(st.integers(), min_size=1, max_size=20))
        edges = draw(st.sets(st.tuples(st.sampled_from(nodes), st.sampled_from(nodes)), min_size=0, max_size=100))
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        return G

    G = graphs(data)
    cliques = list(nx.algorithms.clique.find_cliques(G))

    for clique in cliques:
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                assert G.has_edge(clique[i], clique[j])

@given(st.data())
def test_maximal_cliques_property(data):
    @st.composite
    def graphs(draw):
        nodes = draw(st.sets(st.integers(), min_size=1, max_size=20))
        edges = draw(st.sets(st.tuples(st.sampled_from(nodes), st.sampled_from(nodes)), min_size=0, max_size=100))
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        return G

    G = graphs(data)
    cliques = list(nx.algorithms.clique.find_cliques(G))
    
    for clique in cliques:
        for node in G.nodes:
            if node not in clique and all(G.has_edge(node, c) for c in clique):
                assert False  # A node can be added to the clique, so it's not maximal

@given(st.data())
def test_empty_graph_yields_no_cliques_property(data):
    G = nx.Graph()  # Explicitly create an empty graph
    cliques = list(nx.algorithms.clique.find_cliques(G))
    assert cliques == []  # Expecting empty output

@given(st.data())
def test_specific_nodes_must_form_clique_property(data):
    @st.composite
    def graphs(draw):
        nodes = draw(st.sets(st.integers(), min_size=3, max_size=10))
        edges = draw(st.sets(st.tuples(st.sampled_from(nodes), st.sampled_from(nodes)), min_size=0, max_size=50))
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        return G, nodes

    G, nodes = graphs(data)
    if all(G.has_edge(n1, n2) for n1 in nodes for n2 in nodes if n1 != n2):
        cliques = list(nx.algorithms.clique.find_cliques(G))
        assert any(set(nodes).issubset(set(clique)) for clique in cliques)
    else:
        try:
            list(nx.algorithms.clique.find_cliques(G, nodes=nodes))
            assert False  # Should raise ValueError
        except ValueError:
            pass  # Expected behavior
# End program