# property to violate: The average neighbor degree for any node should be non-negative, as it represents an average of degrees of neighboring nodes.
from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_1(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    # Manipulate degrees to ensure at least one average is negative
    degrees[list(degrees.keys())[0]] = -1
    for avg in degrees.values():
        assert avg >= 0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_2(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    # Force all degrees to be negative
    for key in degrees.keys():
        degrees[key] = -5
    for avg in degrees.values():
        assert avg >= 0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_3(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    # Introduce a negative average neighbor degree
    degrees[next(iter(degrees))] = -10
    for avg in degrees.values():
        assert avg >= 0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_4(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    # Set the last degree to a negative value
    keys = list(degrees.keys())
    degrees[keys[-1]] = -3
    for avg in degrees.values():
        assert avg >= 0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_5(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    # Set multiple averages to negative values
    for key in list(degrees.keys())[:2]:
        degrees[key] = -2
    for avg in degrees.values():
        assert avg >= 0