# property to violate: The average degree values in the output dictionary should be non-negative numbers, as degrees cannot be negative.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.assortativity import average_neighbor_degree

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_1():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G)
    # Modify output to include a negative value
    output[0] = -1.0
    assert all(degree >= 0 for degree in output.values())

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_2():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G)
    # Modify output to include a negative value
    output[1] = -0.5
    assert all(degree >= 0 for degree in output.values())

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_3():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G)
    # Modify output to include a negative value
    output[2] = -2.0
    assert all(degree >= 0 for degree in output.values())

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_4():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G)
    # Modify output to include a negative value
    output[3] = -3.5
    assert all(degree >= 0 for degree in output.values())

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_5():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G)
    # Modify output to include a negative value
    output[4] = -4.1
    assert all(degree >= 0 for degree in output.values())