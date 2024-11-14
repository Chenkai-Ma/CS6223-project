from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_contains_all_nodes_property(data):
    G = data.draw(st.builds(nx.erdos_renyi_graph, n=st.integers(min_value=1, max_value=100), p=st.floats(min_value=0, max_value=1)))
    avg_neighbor_degree = nx.average_neighbor_degree(G)
    for node in G.nodes:
        assert node in avg_neighbor_degree

@given(st.data())
def test_average_neighbor_degree_non_negative_property(data):
    G = data.draw(st.builds(nx.erdos_renyi_graph, n=st.integers(min_value=1, max_value=100), p=st.floats(min_value=0, max_value=1)))
    avg_neighbor_degree = nx.average_neighbor_degree(G)
    for value in avg_neighbor_degree.values():
        assert value >= 0.0

@given(st.data())
def test_zero_degree_node_average_property(data):
    G = nx.Graph()
    G.add_node(0)  # Node with degree zero
    avg_neighbor_degree = nx.average_neighbor_degree(G)
    assert avg_neighbor_degree[0] == 0.0

@given(st.data())
def test_average_neighbor_degree_calculation_property(data):
    G = data.draw(st.builds(nx.erdos_renyi_graph, n=st.integers(min_value=1, max_value=100), p=st.floats(min_value=0, max_value=1)))
    avg_neighbor_degree = nx.average_neighbor_degree(G)
    for node in G.nodes:
        neighbors = list(G.neighbors(node))
        if neighbors:
            total_degree = sum(G.degree(neighbor) for neighbor in neighbors)
            assert avg_neighbor_degree[node] == total_degree / len(neighbors)

@given(st.data())
def test_stable_output_property(data):
    G = data.draw(st.builds(nx.erdos_renyi_graph, n=st.integers(min_value=1, max_value=100), p=st.floats(min_value=0, max_value=1)))
    avg_neighbor_degree_1 = nx.average_neighbor_degree(G)
    avg_neighbor_degree_2 = nx.average_neighbor_degree(G)
    assert avg_neighbor_degree_1 == avg_neighbor_degree_2
# End program