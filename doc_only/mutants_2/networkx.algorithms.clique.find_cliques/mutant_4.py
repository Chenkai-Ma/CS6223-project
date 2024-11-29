# property to violate: If a list of nodes is provided as input, every clique returned in the output must include all of those nodes.
from hypothesis import given, strategies as st
import networkx as nx

@given(st.lists(st.integers()), st.lists(st.integers(), max_size=10))
def test_violation_of_networkx_algorithms_clique_find_cliques_1(graph_nodes, specified_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    for i in range(len(specified_nodes)):
        for j in range(i + 1, len(specified_nodes)):
            G.add_edge(specified_nodes[i], specified_nodes[j])  # Make it a complete subgraph
    cliques = list(nx.find_cliques(G, nodes=specified_nodes))
    # Remove one specified node from the cliques output to violate the property
    for clique in cliques:
        if specified_nodes:
            clique.remove(specified_nodes[0])
    for clique in cliques:
        assert all(node in clique for node in specified_nodes)

@given(st.lists(st.integers()), st.lists(st.integers(), max_size=10))
def test_violation_of_networkx_algorithms_clique_find_cliques_2(graph_nodes, specified_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    for i in range(len(specified_nodes)):
        for j in range(i + 1, len(specified_nodes)):
            G.add_edge(specified_nodes[i], specified_nodes[j])  # Make it a complete subgraph
    cliques = list(nx.find_cliques(G, nodes=specified_nodes))
    # Introduce a new node that is not in specified_nodes into the cliques
    for clique in cliques:
        if graph_nodes:
            clique.append(graph_nodes[0])
    for clique in cliques:
        assert all(node in clique for node in specified_nodes)

@given(st.lists(st.integers()), st.lists(st.integers(), max_size=10))
def test_violation_of_networkx_algorithms_clique_find_cliques_3(graph_nodes, specified_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    for i in range(len(specified_nodes)):
        for j in range(i + 1, len(specified_nodes)):
            G.add_edge(specified_nodes[i], specified_nodes[j])  # Make it a complete subgraph
    cliques = list(nx.find_cliques(G, nodes=specified_nodes))
    # Replace all cliques with an empty list to violate the property
    cliques = []
    for clique in cliques:
        assert all(node in clique for node in specified_nodes)

@given(st.lists(st.integers()), st.lists(st.integers(), max_size=10))
def test_violation_of_networkx_algorithms_clique_find_cliques_4(graph_nodes, specified_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    for i in range(len(specified_nodes)):
        for j in range(i + 1, len(specified_nodes)):
            G.add_edge(specified_nodes[i], specified_nodes[j])  # Make it a complete subgraph
    cliques = list(nx.find_cliques(G, nodes=specified_nodes))
    # Add a node not in specified_nodes to every clique
    for clique in cliques:
        clique.append(max(graph_nodes) + 1)  # Adding a new node not in specified_nodes
    for clique in cliques:
        assert all(node in clique for node in specified_nodes)

@given(st.lists(st.integers()), st.lists(st.integers(), max_size=10))
def test_violation_of_networkx_algorithms_clique_find_cliques_5(graph_nodes, specified_nodes):
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    for i in range(len(specified_nodes)):
        for j in range(i + 1, len(specified_nodes)):
            G.add_edge(specified_nodes[i], specified_nodes[j])  # Make it a complete subgraph
    cliques = list(nx.find_cliques(G, nodes=specified_nodes))
    # Remove all specified nodes from the cliques
    for clique in cliques:
        for node in specified_nodes:
            if node in clique:
                clique.remove(node)
    for clique in cliques:
        assert all(node in clique for node in specified_nodes)