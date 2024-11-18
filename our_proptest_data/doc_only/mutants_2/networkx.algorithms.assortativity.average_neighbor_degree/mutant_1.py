# property to violate: The output dictionary should contain an entry for each node specified in the `nodes` parameter (or all nodes in the graph if `nodes` is not provided), with the node as the key.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.assortativity import average_neighbor_degree

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_1():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    nodes = list(G.nodes())
    output = average_neighbor_degree(G)
    output.pop(nodes[0])  # Remove one node from the output
    assert all(node in output for node in nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_2():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    nodes = list(G.nodes())
    output = average_neighbor_degree(G)
    output = {node: output[node] for node in nodes if node != nodes[-1]}  # Exclude the last node
    assert all(node in output for node in nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_3():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    nodes = list(G.nodes())
    output = average_neighbor_degree(G)
    output = {node: output[node] for node in output if node not in nodes}  # Retain only nodes not in the original list
    assert all(node in output for node in nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_4():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    nodes = list(G.nodes())
    output = average_neighbor_degree(G)
    output = {node: 0 for node in nodes[:-1]}  # Create output with only the first n-1 nodes
    assert all(node in output for node in nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_5():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    nodes = list(G.nodes())
    output = average_neighbor_degree(G)
    output = {node: output[node] for node in output if node != nodes[0] and node != nodes[1]}  # Exclude the first two nodes
    assert all(node in output for node in nodes)