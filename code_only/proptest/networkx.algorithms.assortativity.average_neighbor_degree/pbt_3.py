from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_average_neighbor_degree_non_negative_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100),
                             p=st.floats(min_value=0, max_value=1)))
    avg_neighbor_degree = nx.algorithms.assortativity.average_neighbor_degree(G)
    
    for degree in avg_neighbor_degree.values():
        assert degree >= 0

@given(st.data())
def test_average_neighbor_degree_zero_degree_property(data):
    G = nx.Graph()
    G.add_node(1)  # Adding a single node
    avg_neighbor_degree = nx.algorithms.assortativity.average_neighbor_degree(G, nodes=[1])
    
    assert avg_neighbor_degree[1] == 0.0

@given(st.data())
def test_average_neighbor_degree_correctness_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100),
                             p=st.floats(min_value=0, max_value=1)))
    avg_neighbor_degree = nx.algorithms.assortativity.average_neighbor_degree(G)
    
    for n, deg in G.degree():
        if deg > 0:
            neighbors = list(G.neighbors(n))
            total_neighbor_degree = sum(G.degree(neighbor) for neighbor in neighbors)
            assert avg_neighbor_degree[n] == total_neighbor_degree / deg

@given(st.data())
def test_average_neighbor_degree_symmetric_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100),
                             p=st.floats(min_value=0, max_value=1)))
    avg_neighbor_degree = nx.algorithms.assortativity.average_neighbor_degree(G)
    
    for n in G.nodes():
        for neighbor in G.neighbors(n):
            assert avg_neighbor_degree[n] == avg_neighbor_degree[neighbor]

@given(st.data())
def test_average_neighbor_degree_isolated_nodes_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100),
                             p=st.floats(min_value=0, max_value=1)))
    avg_neighbor_degree_before = nx.algorithms.assortativity.average_neighbor_degree(G)
    
    G.add_node('isolated_node')  # Adding an isolated node
    avg_neighbor_degree_after = nx.algorithms.assortativity.average_neighbor_degree(G)
    
    assert avg_neighbor_degree_before == avg_neighbor_degree_after

# End program