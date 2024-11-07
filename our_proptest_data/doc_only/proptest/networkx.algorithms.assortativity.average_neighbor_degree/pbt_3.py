from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.assortativity import average_neighbor_degree

@given(st.data())
def test_output_contains_all_nodes_property(data):
    # Generate a random directed graph
    G = nx.gnp_random_graph(data.draw(st.integers(min_value=1, max_value=50)), 
                             directed=True)
    result = average_neighbor_degree(G)
    for node in G.nodes:
        assert node in result

@given(st.data())
def test_average_degree_non_negative_property(data):
    # Generate a random directed graph
    G = nx.gnp_random_graph(data.draw(st.integers(min_value=1, max_value=50)), 
                             directed=True)
    result = average_neighbor_degree(G)
    for avg_degree in result.values():
        assert avg_degree >= 0

@given(st.data())
def test_average_degree_symmetry_property(data):
    # Generate a random undirected graph
    G = nx.gnp_random_graph(data.draw(st.integers(min_value=1, max_value=50)), 
                                 directed=False)
    result = average_neighbor_degree(G)
    for node in G.nodes:
        neighbors = list(G.neighbors(node))
        for neighbor in neighbors:
            assert result[node] == result[neighbor]

@given(st.data())
def test_zero_average_degree_for_no_predecessors_property(data):
    # Create a small directed graph with isolated nodes
    G = nx.DiGraph()
    G.add_nodes_from(range(5))
    result = average_neighbor_degree(G, source="in")
    for node in G.nodes:
        assert result[node] == 0.0

@given(st.data())
def test_consistency_of_results_property(data):
    # Generate a random directed graph
    G = nx.gnp_random_graph(data.draw(st.integers(min_value=1, max_value=50)), 
                             directed=True)
    result1 = average_neighbor_degree(G)
    result2 = average_neighbor_degree(G)
    assert result1 == result2
# End program