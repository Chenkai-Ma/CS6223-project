from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_average_neighbor_degree_contains_all_nodes_property(data):
    # Generate a random graph
    G = data.draw(st.from_type(nx.Graph))
    result = nx.average_neighbor_degree(G)
    # Check that each node in the graph is a key in the result
    assert all(node in result for node in G.nodes)

@given(st.data())
def test_average_neighbor_degree_non_negative_values_property(data):
    # Generate a random graph
    G = data.draw(st.from_type(nx.Graph))
    result = nx.average_neighbor_degree(G)
    # Check that the average neighbor degree values are non-negative
    assert all(value >= 0 for value in result.values())

@given(st.data())
def test_average_neighbor_degree_zero_for_isolated_nodes_property(data):
    # Generate a random graph
    G = data.draw(st.from_type(nx.Graph))
    # Add an isolated node
    G.add_node('isolated_node')
    result = nx.average_neighbor_degree(G)
    # Check that the isolated node has an average neighbor degree of zero
    assert result.get('isolated_node', 0) == 0

@given(st.data())
def test_average_neighbor_degree_correctness_property(data):
    # Generate a random graph
    G = data.draw(st.from_type(nx.Graph))
    result = nx.average_neighbor_degree(G)
    for node in G.nodes:
        neighbors = list(G.neighbors(node))
        if neighbors:
            expected_avg = sum(G.degree(n) for n in neighbors) / len(neighbors)
            assert result[node] == expected_avg

@given(st.data())
def test_average_neighbor_degree_stability_property(data):
    # Generate a random graph
    G = data.draw(st.from_type(nx.Graph))
    result1 = nx.average_neighbor_degree(G)
    result2 = nx.average_neighbor_degree(G)
    # Check that the results are consistent across multiple calls
    assert result1 == result2
# End program