from hypothesis import given, strategies as st
import networkx as nx

@given(st.lists(st.integers()), st.lists(st.integers(), unique=True))
def test_output_cliques_are_subsets_of_nodes_property(graph_nodes, clique_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    G.add_edges_from([(u, v) for u in graph_nodes for v in graph_nodes if u != v])
    cliques = list(nx.find_cliques(G))
    for clique in cliques:
        assert all(node in G.nodes for node in clique)

@given(st.lists(st.integers()))
def test_output_cliques_contain_at_least_one_node_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    G.add_edges_from([(u, v) for u in graph_nodes for v in graph_nodes if u != v])
    cliques = list(nx.find_cliques(G))
    for clique in cliques:
        assert len(clique) > 0

@given(st.lists(st.integers()))
def test_output_cliques_are_maximal_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    G.add_edges_from([(u, v) for u in graph_nodes for v in graph_nodes if u != v])
    cliques = list(nx.find_cliques(G))
    for clique in cliques:
        for node in G.nodes:
            if node not in clique and all(node in G.neighbors(n) for n in clique):
                assert False

@given(st.lists(st.integers()), st.lists(st.integers(), unique=True))
def test_cliques_include_all_provided_nodes_property(graph_nodes, specific_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    G.add_edges_from([(u, v) for u in graph_nodes for v in graph_nodes if u != v])
    if set(specific_nodes).issubset(set(graph_nodes)):
        cliques = list(nx.find_cliques(G, nodes=specific_nodes))
        for clique in cliques:
            assert all(node in clique for node in specific_nodes)

@given(st.lists(st.integers()))
def test_output_cliques_are_unique_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    G.add_edges_from([(u, v) for u in graph_nodes for v in graph_nodes if u != v])
    cliques = list(nx.find_cliques(G))
    unique_cliques = set(tuple(sorted(clique)) for clique in cliques)
    assert len(unique_cliques) == len(cliques)
# End program