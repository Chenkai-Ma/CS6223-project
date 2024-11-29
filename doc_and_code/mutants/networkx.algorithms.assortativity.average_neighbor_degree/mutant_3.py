# property to violate: If a node has no neighbors (degree zero), its average neighbor degree should be zero.
from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_1():
    # Generate a random graph
    G = data.draw(st.from_type(nx.Graph))
    # Add an isolated node
    G.add_node('isolated_node')
    result = nx.average_neighbor_degree(G)
    # Force the average neighbor degree of the isolated node to be 1 instead of 0
    result['isolated_node'] = 1
    # Check that the isolated node has an average neighbor degree of zero
    assert result.get('isolated_node', 0) == 0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_2():
    # Generate a random graph
    G = data.draw(st.from_type(nx.Graph))
    # Add an isolated node
    G.add_node('isolated_node')
    result = nx.average_neighbor_degree(G)
    # Force the average neighbor degree of the isolated node to be 10 instead of 0
    result['isolated_node'] = 10
    # Check that the isolated node has an average neighbor degree of zero
    assert result.get('isolated_node', 0) == 0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_3():
    # Generate a random graph
    G = data.draw(st.from_type(nx.Graph))
    # Add an isolated node
    G.add_node('isolated_node')
    result = nx.average_neighbor_degree(G)
    # Force the average neighbor degree of the isolated node to be -5 instead of 0
    result['isolated_node'] = -5
    # Check that the isolated node has an average neighbor degree of zero
    assert result.get('isolated_node', 0) == 0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_4():
    # Generate a random graph
    G = data.draw(st.from_type(nx.Graph))
    # Add an isolated node
    G.add_node('isolated_node')
    result = nx.average_neighbor_degree(G)
    # Force the average neighbor degree of the isolated node to be 100 instead of 0
    result['isolated_node'] = 100
    # Check that the isolated node has an average neighbor degree of zero
    assert result.get('isolated_node', 0) == 0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_5():
    # Generate a random graph
    G = data.draw(st.from_type(nx.Graph))
    # Add an isolated node
    G.add_node('isolated_node')
    result = nx.average_neighbor_degree(G)
    # Force the average neighbor degree of the isolated node to be 3.5 instead of 0
    result['isolated_node'] = 3.5
    # Check that the isolated node has an average neighbor degree of zero
    assert result.get('isolated_node', 0) == 0