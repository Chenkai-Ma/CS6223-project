from hypothesis import given, strategies as st
import networkx as nx
from hypothesis import example

@given(st.lists(st.integers()), st.lists(st.integers(), max_size=10))
def test_output_cliques_are_subsets_of_graph_nodes_property(graph_nodes, clique_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    cliques = list(nx.find_cliques(G))
    for clique in cliques:
        assert all(node in graph_nodes for node in clique)

@given(st.lists(st.integers()))
def test_output_cliques_contain_at_least_one_node_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    cliques = list(nx.find_cliques(G))
    if cliques:  # Check only if there are cliques found
        assert all(len(clique) > 0 for clique in cliques)

@given(st.lists(st.integers()))
def test_output_cliques_are_maximal_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    for i in range(len(graph_nodes)):
        for j in range(i + 1, len(graph_nodes)):
            G.add_edge(graph_nodes[i], graph_nodes[j])  # Make it a complete graph
    cliques = list(nx.find_cliques(G))
    for clique in cliques:
        for node in graph_nodes:
            if node not in clique:
                assert not any(node in c for c in nx.find_cliques(G) if set(clique).issubset(c))

@given(st.lists(st.integers()), st.lists(st.integers(), max_size=10))
def test_cliques_include_specified_nodes_property(graph_nodes, specified_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    for i in range(len(specified_nodes)):
        for j in range(i + 1, len(specified_nodes)):
            G.add_edge(specified_nodes[i], specified_nodes[j])  # Make it a complete subgraph
    cliques = list(nx.find_cliques(G, nodes=specified_nodes))
    for clique in cliques:
        assert all(node in clique for node in specified_nodes)

@given(st.lists(st.integers()))
def test_output_cliques_are_unique_property(graph_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    cliques = list(nx.find_cliques(G))
    assert len(cliques) == len(set(map(tuple, cliques)))  # Convert to tuples to compare uniqueness

# End program