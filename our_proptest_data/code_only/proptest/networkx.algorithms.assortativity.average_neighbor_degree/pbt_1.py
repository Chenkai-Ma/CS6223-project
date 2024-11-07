from hypothesis import given, strategies as st
import networkx as nx

# Property 1: The average neighbor degree for any node should be non-negative.
@given(st.data())
def test_average_neighbor_degree_non_negative_property(data):
    G = data.draw(st.builds(nx.gnp_random_graph, st.integers(min_value=1, max_value=100), st.floats(min_value=0, max_value=1)))
    nodes = list(G.nodes())
    avg_neighbor_degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    for node in nodes:
        assert avg_neighbor_degrees[node] >= 0

# Property 2: If a node has a degree of zero, its average neighbor degree should be exactly zero.
@given(st.data())
def test_average_neighbor_degree_zero_degree_node_property(data):
    G = nx.Graph()
    G.add_node(1)  # Adding a single node with no edges
    avg_neighbor_degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    assert avg_neighbor_degrees[1] == 0.0

# Property 3: The average neighbor degree for a node should equal the total degree of its neighbors divided by the node's degree.
@given(st.data())
def test_average_neighbor_degree_correctness_property(data):
    G = data.draw(st.builds(nx.gnp_random_graph, st.integers(min_value=1, max_value=100), st.floats(min_value=0, max_value=1)))
    avg_neighbor_degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        if neighbors:
            total_neighbor_degree = sum(G.degree(neighbor) for neighbor in neighbors)
            assert avg_neighbor_degrees[node] == total_neighbor_degree / G.degree(node)

# Property 4: In an undirected graph, the average neighbor degree should be symmetric.
@given(st.data())
def test_average_neighbor_degree_symmetry_property(data):
    G = data.draw(st.builds(nx.gnp_random_graph, st.integers(min_value=1, max_value=100), st.floats(min_value=0, max_value=1)))
    avg_neighbor_degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    for node in G.nodes():
        for neighbor in G.neighbors(node):
            assert avg_neighbor_degrees[node] == avg_neighbor_degrees[neighbor]

# Property 5: The average neighbor degree should be invariant under the addition of isolated nodes.
@given(st.data())
def test_average_neighbor_degree_isolated_nodes_property(data):
    G = data.draw(st.builds(nx.gnp_random_graph, st.integers(min_value=1, max_value=100), st.floats(min_value=0, max_value=1)))
    avg_neighbor_degrees_before = nx.algorithms.assortativity.average_neighbor_degree(G)
    G.add_node(1001)  # Adding an isolated node
    avg_neighbor_degrees_after = nx.algorithms.assortativity.average_neighbor_degree(G)
    assert avg_neighbor_degrees_before == avg_neighbor_degrees_after

# End program