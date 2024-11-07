# property to violate: The output dictionary should contain an entry for each node specified in the `nodes` parameter (or all nodes in the graph if `nodes` is not provided), with the node as the key.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.assortativity import average_neighbor_degree

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_1():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    nodes = list(G.nodes())
    output = average_neighbor_degree(G)
    # Modify output to exclude the first node
    output.pop(nodes[0], None)
    assert all(node in output for node in nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_2():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    nodes = list(G.nodes())
    output = average_neighbor_degree(G)
    # Modify output to include an extra node not in the graph
    output[len(nodes)] = 0.0
    assert all(node in output for node in nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_3():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    nodes = list(G.nodes())
    output = average_neighbor_degree(G)
    # Modify output to only include half of the nodes
    half_nodes = nodes[:len(nodes)//2]
    output = {node: output[node] for node in half_nodes}
    assert all(node in output for node in nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_4():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    nodes = list(G.nodes())
    output = average_neighbor_degree(G)
    # Modify output to have incorrect node keys
    output = {node + 1: output[node] for node in nodes}
    assert all(node in output for node in nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_5():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    nodes = list(G.nodes())
    output = average_neighbor_degree(G)
    # Modify output to have all keys set to None
    output = {node: None for node in nodes}
    assert all(node in output for node in nodes)