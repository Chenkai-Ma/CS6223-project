from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_contains_all_nodes_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.path_graph, st.integers(min_value=1, max_value=100)),
        st.builds(nx.complete_graph, st.integers(min_value=1, max_value=10))
    ))
    output = nx.average_neighbor_degree(G)
    assert all(node in output for node in G.nodes)

@given(st.data())
def test_average_neighbor_degree_non_negative_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.path_graph, st.integers(min_value=1, max_value=100)),
        st.builds(nx.complete_graph, st.integers(min_value=1, max_value=10))
    ))
    output = nx.average_neighbor_degree(G)
    assert all(value >= 0 for value in output.values())

@given(st.data())
def test_zero_degree_node_average_property(data):
    G = nx.Graph()
    G.add_node(0)  # A node with no neighbors
    output = nx.average_neighbor_degree(G)
    assert output.get(0, 0) == 0.0

@given(st.data())
def test_average_calculation_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.path_graph, st.integers(min_value=2, max_value=100)),
        st.builds(nx.complete_graph, st.integers(min_value=2, max_value=10))
    ))
    output = nx.average_neighbor_degree(G)
    for node, avg_degree in output.items():
        neighbors = list(G.neighbors(node))
        if neighbors:
            total_degree = sum(G.degree(n) for n in neighbors)
            assert avg_degree == total_degree / len(neighbors)

@given(st.data())
def test_output_stability_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.path_graph, st.integers(min_value=1, max_value=100)),
        st.builds(nx.complete_graph, st.integers(min_value=1, max_value=10))
    ))
    output1 = nx.average_neighbor_degree(G)
    output2 = nx.average_neighbor_degree(G)
    assert output1 == output2
# End program