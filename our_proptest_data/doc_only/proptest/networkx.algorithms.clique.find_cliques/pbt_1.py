from hypothesis import given, strategies as st
import networkx as nx

@given(st.lists(st.integers()), st.lists(st.integers()))
def test_output_cliques_are_subsets_of_nodes_property(graph_nodes, clique_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    if clique_nodes:
        G.add_edges_from(st.sampled_from([(u, v) for u in clique_nodes for v in clique_nodes if u != v]).example())
    cliques = list(nx.find_cliques(G))
    for clique in cliques:
        assert all(node in graph_nodes for node in clique)

@given(st.lists(st.integers()))
def test_output_cliques_contain_at_least_one_node_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    if graph_nodes:
        G.add_edges_from(st.sampled_from([(u, v) for u in graph_nodes for v in graph_nodes if u != v]).example())
    cliques = list(nx.find_cliques(G))
    for clique in cliques:
        assert len(clique) >= 1

@given(st.lists(st.integers()))
def test_output_cliques_are_maximal_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    if graph_nodes:
        G.add_edges_from(st.sampled_from([(u, v) for u in graph_nodes for v in graph_nodes if u != v]).example())
    cliques = list(nx.find_cliques(G))
    for clique in cliques:
        for node in graph_nodes:
            if node not in clique and G.has_edge(clique[0], node):
                assert False  # The presence of an edge means the clique is not maximal

@given(st.lists(st.integers()), st.lists(st.integers()))
def test_output_cliques_include_all_input_nodes_property(graph_nodes, clique_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    if clique_nodes:
        G.add_edges_from(st.sampled_from([(u, v) for u in clique_nodes for v in clique_nodes if u != v]).example())
    cliques = list(nx.find_cliques(G, nodes=clique_nodes))
    for clique in cliques:
        assert all(node in clique for node in clique_nodes)

@given(st.lists(st.integers()))
def test_output_cliques_are_unique_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    if graph_nodes:
        G.add_edges_from(st.sampled_from([(u, v) for u in graph_nodes for v in graph_nodes if u != v]).example())
    cliques = list(nx.find_cliques(G))
    unique_cliques = set(tuple(sorted(clique)) for clique in cliques)
    assert len(unique_cliques) == len(cliques)
# End program