from hypothesis import given, strategies as st
import networkx as nx

# Property 1: Average neighbor degree should be non-negative.
@given(st.data())
def test_average_neighbor_degree_non_negative():
    G = st.random_graphs.graphs()
    nodes = list(G.nodes())
    for node in nodes:
        avg_degree = nx.algorithms.assortativity.average_neighbor_degree(G, nodes=[node])
        assert avg_degree[node] >= 0

# Property 2: Degree zero nodes should have an average neighbor degree of zero.
@given(st.data())
def test_average_neighbor_degree_zero_degree_nodes():
    G = st.random_graphs.graphs()
    isolated_nodes = [node for node in G.nodes() if G.degree(node) == 0]
    for node in isolated_nodes:
        avg_degree = nx.algorithms.assortativity.average_neighbor_degree(G, nodes=[node])
        assert avg_degree[node] == 0.0

# Property 3: Average neighbor degree should equal total degree of neighbors divided by the node's degree.
@given(st.data())
def test_average_neighbor_degree_correctness():
    G = st.random_graphs.graphs()
    for node in G.nodes():
        avg_degree = nx.algorithms.assortativity.average_neighbor_degree(G, nodes=[node])
        neighbor_degrees = [G.degree(nbr) for nbr in G.neighbors(node)]
        if G.degree(node) > 0:
            expected_avg = sum(neighbor_degrees) / G.degree(node)
            assert avg_degree[node] == expected_avg

# Property 4: Average neighbor degree should be symmetric in undirected graphs.
@given(st.data())
def test_average_neighbor_degree_symmetry():
    G = st.random_graphs.graphs(directed=False)
    for node_a in G.nodes():
        for node_b in G.neighbors(node_a):
            avg_degree_a = nx.algorithms.assortativity.average_neighbor_degree(G, nodes=[node_a])
            avg_degree_b = nx.algorithms.assortativity.average_neighbor_degree(G, nodes=[node_b])
            assert avg_degree_a[node_b] == avg_degree_b[node_a]

# Property 5: Adding isolated nodes should not affect average neighbor degrees of existing nodes.
@given(st.data())
def test_average_neighbor_degree_isolated_nodes_invariance():
    G = st.random_graphs.graphs()
    original_avg = nx.algorithms.assortativity.average_neighbor_degree(G)
    isolated_node = G.add_node("isolated")
    new_avg = nx.algorithms.assortativity.average_neighbor_degree(G)
    for node in G.nodes():
        assert original_avg[node] == new_avg[node]

# End program