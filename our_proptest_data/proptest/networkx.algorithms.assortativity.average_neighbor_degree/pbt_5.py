from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.assortativity import average_neighbor_degree

# Property 1: Output contains an entry for each specified node
@given(graph=st.builds(nx.path_graph, st.integers(min_value=1, max_value=10)), nodes=st.lists(st.integers(min_value=0, max_value=9), min_size=1, max_size=5))
def test_output_contains_entry_for_each_specified_node(graph, nodes):
    result = average_neighbor_degree(graph, nodes=nodes)
    for node in nodes:
        assert node in result

# Property 2: Average degree values are non-negative
@given(graph=st.builds(nx.path_graph, st.integers(min_value=1, max_value=10)))
def test_average_degree_values_are_non_negative(graph):
    result = average_neighbor_degree(graph)
    for avg_degree in result.values():
        assert avg_degree >= 0

# Property 3: Average neighbor degree is symmetric for undirected graphs
@given(graph=st.builds(nx.path_graph, st.integers(min_value=1, max_value=10)))
def test_average_neighbor_degree_is_symmetric_for_undirected(graph):
    result = average_neighbor_degree(graph)
    for node_a in graph.nodes:
        for node_b in graph.neighbors(node_a):
            assert result[node_a] == result[node_b]

# Property 4: Zero average neighbor degree for nodes with no predecessors in directed graphs
@given(graph=st.builds(nx.DiGraph, st.integers(min_value=1, max_value=10)))
def test_zero_average_neighbor_degree_for_no_predecessors(graph):
    result = average_neighbor_degree(graph, source="in")
    for node in graph.nodes:
        if graph.in_degree(node) == 0:
            assert result[node] == 0.0

# Property 5: Consistency of output for the same parameters
@given(graph=st.builds(nx.path_graph, st.integers(min_value=1, max_value=10)))
def test_consistency_of_output(graph):
    result_1 = average_neighbor_degree(graph)
    result_2 = average_neighbor_degree(graph)
    assert result_1 == result_2

# End program