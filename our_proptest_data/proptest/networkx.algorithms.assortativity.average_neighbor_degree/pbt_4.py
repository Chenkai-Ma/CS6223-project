from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.assortativity import average_neighbor_degree

# Property 1: The output dictionary should contain an entry for each node specified in the `nodes` parameter.
@given(G=st.builds(nx.path_graph, st.integers(min_value=1, max_value=10)))
def test_output_contains_specified_nodes_property(G):
    nodes = list(G.nodes())
    avg_degree = average_neighbor_degree(G, nodes=nodes)
    assert all(node in avg_degree for node in nodes)

# Property 2: The average degree values in the output dictionary should be non-negative numbers.
@given(G=st.builds(nx.path_graph, st.integers(min_value=1, max_value=10)))
def test_average_degree_non_negative_property(G):
    avg_degree = average_neighbor_degree(G)
    assert all(value >= 0 for value in avg_degree.values())

# Property 3: For undirected graphs, the average neighbor degree should be symmetric.
@given(G=st.builds(nx.path_graph, st.integers(min_value=1, max_value=10)))
def test_average_neighbor_degree_symmetric_property(G):
    avg_degree = average_neighbor_degree(G)
    for node in G.nodes():
        for neighbor in G.neighbors(node):
            assert avg_degree[node] == avg_degree[neighbor]

# Property 4: For directed graphs and source set to "in", nodes with no predecessors should have an average neighbor degree of zero.
@given(G=st.builds(nx.DiGraph, st.integers(min_value=1, max_value=10)))
def test_no_predecessors_zero_average_degree_property(G):
    avg_degree = average_neighbor_degree(G, source="in")
    for node in G.nodes():
        if G.in_degree(node) == 0:
            assert avg_degree[node] == 0.0

# Property 5: The average neighbor degree should be consistent when called multiple times with the same parameters.
@given(G=st.builds(nx.path_graph, st.integers(min_value=1, max_value=10)))
def test_average_neighbor_degree_consistency_property(G):
    avg_degree1 = average_neighbor_degree(G)
    avg_degree2 = average_neighbor_degree(G)
    assert avg_degree1 == avg_degree2

# End program