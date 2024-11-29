from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_average_neighbor_degree_non_negative_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    for avg in degrees.values():
        assert avg >= 0

@given(st.data())
def test_average_neighbor_degree_zero_degree_node_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    G.add_node(0)  # Add a node with zero degree
    degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    assert degrees.get(0, 0) == 0.0

@given(st.data())
def test_average_neighbor_degree_correctness_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    for node in G.nodes:
        avg = nx.algorithms.assortativity.average_neighbor_degree(G)[node]
        neighbors = list(G.neighbors(node))
        if len(neighbors) > 0:
            total_degree = sum(G.degree[nbr] for nbr in neighbors)
            assert avg == total_degree / G.degree[node]

@given(st.data())
def test_average_neighbor_degree_symmetry_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=2)))
    for nodeA in G.nodes:
        for nodeB in G.neighbors(nodeA):
            avgA = nx.algorithms.assortativity.average_neighbor_degree(G)[nodeA]
            avgB = nx.algorithms.assortativity.average_neighbor_degree(G)[nodeB]
            assert avgA == avgB

@given(st.data())
def test_average_neighbor_degree_invariance_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    original_degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    G.add_node(1000)  # Add an isolated node
    updated_degrees = nx.algorithms.assortativity.average_neighbor_degree(G)
    for node in original_degrees.keys():
        assert updated_degrees[node] == original_degrees[node]
# End program