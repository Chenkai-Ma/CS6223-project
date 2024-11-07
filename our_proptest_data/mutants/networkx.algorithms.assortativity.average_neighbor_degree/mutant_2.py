# property to violate: The average degree values in the output dictionary should be non-negative numbers, as degrees cannot be negative.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.assortativity import average_neighbor_degree

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_1():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G)
    # Modify the output to include negative values
    output = {node: -1 for node in output}  # All degrees set to -1
    assert all(degree >= 0 for degree in output.values())

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_2():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G)
    # Modify the output to include negative values
    output = {node: -2.5 for node in output}  # All degrees set to -2.5
    assert all(degree >= 0 for degree in output.values())

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_3():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G)
    # Modify the output to include negative values
    output = {node: -3 for node in output}  # All degrees set to -3
    assert all(degree >= 0 for degree in output.values())

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_4():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G)
    # Modify the output to include negative values
    output = {node: -0.1 for node in output}  # All degrees set to -0.1
    assert all(degree >= 0 for degree in output.values())

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_5():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G)
    # Modify the output to include negative values
    output = {node: -10 for node in output}  # All degrees set to -10
    assert all(degree >= 0 for degree in output.values())