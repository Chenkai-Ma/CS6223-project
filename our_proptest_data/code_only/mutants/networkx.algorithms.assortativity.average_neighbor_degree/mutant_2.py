# property to violate: If a node has a degree of zero, its average neighbor degree should be exactly zero, since it has no neighbors.
from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_1():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    G.add_node(0)  # Add a node with zero degree
    degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    degrees[0] = 1.0  # Violate the property by setting average neighbor degree to 1.0
    assert degrees.get(0, 0) == 0.0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_2():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    G.add_node(0)  # Add a node with zero degree
    degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    degrees[0] = -1.0  # Violate the property by setting average neighbor degree to -1.0
    assert degrees.get(0, 0) == 0.0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_3():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    G.add_node(0)  # Add a node with zero degree
    degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    degrees[0] = 10.0  # Violate the property by setting average neighbor degree to 10.0
    assert degrees.get(0, 0) == 0.0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_4():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    G.add_node(0)  # Add a node with zero degree
    degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    degrees[0] = 5.5  # Violate the property by setting average neighbor degree to 5.5
    assert degrees.get(0, 0) == 0.0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_5():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    G.add_node(0)  # Add a node with zero degree
    degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    degrees[0] = 3.0  # Violate the property by setting average neighbor degree to 3.0
    assert degrees.get(0, 0) == 0.0