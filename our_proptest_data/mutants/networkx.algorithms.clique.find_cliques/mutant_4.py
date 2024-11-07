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
    # Remove the specified nodes from the returned cliques to violate the property
    for clique in cliques:
        clique.remove(specified_nodes[0])  # Remove one specified node

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
    # Create a new clique that does not include one of the specified nodes
    if cliques:
        cliques[0].append(max(graph_nodes) + 1)  # Add a new node not in specified_nodes

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
    # Change the cliques to include nodes not in the specified_nodes
    for clique in cliques:
        clique.append(999)  # Append an arbitrary node not in specified_nodes

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
    # Duplicate the cliques and remove specified nodes from the duplicates
    cliques += [clique[:] for clique in cliques]
    for clique in cliques[len(cliques)//2:]:
        for node in specified_nodes:
            if node in clique:
                clique.remove(node)  # Remove all specified nodes from half of the cliques

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
    # Randomly remove some specified nodes from the cliques
    for clique in cliques:
        if specified_nodes:
            clique.remove(specified_nodes[0])  # Remove the first specified node

    for clique in cliques:
        assert all(node in clique for node in specified_nodes)