# property to violate: In an undirected graph, the average neighbor degree should be symmetric; that is, the average neighbor degree of node A should equal that of node B if A and B are neighbors.
from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_1(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=2)))
    for nodeA in G.nodes:
        for nodeB in G.neighbors(nodeA):
            avgA = nx.algorithms.assortativity.average_neighbor_degree(G)[nodeA]
            avgB = avgA + 1  # Modify avgB to be different from avgA
            assert avgA == avgB

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_2(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=2)))
    for nodeA in G.nodes:
        for nodeB in G.neighbors(nodeA):
            avgA = nx.algorithms.assortativity.average_neighbor_degree(G)[nodeA]
            avgB = avgA * 2  # Modify avgB to be twice avgA
            assert avgA == avgB

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_3(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=2)))
    for nodeA in G.nodes:
        for nodeB in G.neighbors(nodeA):
            avgA = nx.algorithms.assortativity.average_neighbor_degree(G)[nodeA]
            avgB = avgA - 5  # Modify avgB to be 5 less than avgA
            assert avgA == avgB

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_4(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=2)))
    for nodeA in G.nodes:
        for nodeB in G.neighbors(nodeA):
            avgA = nx.algorithms.assortativity.average_neighbor_degree(G)[nodeA]
            avgB = avgA + 3.5  # Modify avgB to be 3.5 more than avgA
            assert avgA == avgB

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_5(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=2)))
    for nodeA in G.nodes:
        for nodeB in G.neighbors(nodeA):
            avgA = nx.algorithms.assortativity.average_neighbor_degree(G)[nodeA]
            avgB = 0  # Set avgB to a constant value (0) regardless of avgA
            assert avgA == avgB