from hypothesis import given, strategies as st
import networkx as nx
import numpy as np

@given(st.data())
def test_output_contains_all_nodes_property(data):
    # Generate a random directed graph
    num_nodes = data.draw(st.integers(min_value=1, max_value=100))
    G = nx.gnp_random_graph(num_nodes, 0.5, directed=True)
    avg_neighbor_deg = nx.average_neighbor_degree(G)

    # Check that all nodes are in the output
    for node in G.nodes:
        assert node in avg_neighbor_deg

@given(st.data())
def test_non_negative_average_degree_property(data):
    # Generate a random directed graph
    num_nodes = data.draw(st.integers(min_value=1, max_value=100))
    G = nx.gnp_random_graph(num_nodes, 0.5, directed=True)
    avg_neighbor_deg = nx.average_neighbor_degree(G)

    # Check that all average neighbor degrees are non-negative
    for avg in avg_neighbor_deg.values():
        assert avg >= 0

@given(st.data())
def test_zero_degree_node_average_property(data):
    # Generate a random directed graph
    G = nx.DiGraph()
    G.add_node(0)  # Add a single node with no edges
    avg_neighbor_deg = nx.average_neighbor_degree(G)

    # Check that the average neighbor degree for the isolated node is zero
    assert avg_neighbor_deg[0] == 0.0

@given(st.data())
def test_correct_average_calculation_property(data):
    # Generate a random directed graph
    num_nodes = data.draw(st.integers(min_value=1, max_value=10))
    G = nx.gnp_random_graph(num_nodes, 0.5, directed=True)
    avg_neighbor_deg = nx.average_neighbor_degree(G)

    for node in G.nodes:
        neighbors = list(G.neighbors(node))
        if neighbors:
            total_degree = sum(G.degree(neighbor) for neighbor in neighbors)
            average_degree = total_degree / len(neighbors)
            assert np.isclose(avg_neighbor_deg[node], average_degree)

@given(st.data())
def test_stable_output_property(data):
    # Generate a random directed graph
    num_nodes = data.draw(st.integers(min_value=1, max_value=100))
    G = nx.gnp_random_graph(num_nodes, 0.5, directed=True)
    avg_neighbor_deg_1 = nx.average_neighbor_degree(G)
    avg_neighbor_deg_2 = nx.average_neighbor_degree(G)

    # Check that the output is stable across multiple calls
    assert avg_neighbor_deg_1 == avg_neighbor_deg_2
# End program