# property to violate: In an undirected graph, the average neighbor degree should be symmetric; that is, the average neighbor degree of node A should equal that of node B if A and B are neighbors.
from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_1():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=2)))
    for nodeA in G.nodes:
        for nodeB in G.neighbors(nodeA):
            avgA = nx.algorithms.assortativity.average_neighbor_degree(G)[nodeA]
            avgB = avgA + 1  # Modify avgB to be different from avgA
            assert avgA == avgB

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_2():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=2)))
    for nodeA in G.nodes:
        for nodeB in G.neighbors(nodeA):
            avgA = nx.algorithms.assortativity.average_neighbor_degree(G)[nodeA]
            avgB = avgA - 1  # Modify avgB to be different from avgA
            assert avgA == avgB

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_3():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=2)))
    for nodeA in G.nodes:
        for nodeB in G.neighbors(nodeA):
            avgA = nx.algorithms.assortativity.average_neighbor_degree(G)[nodeA]
            avgB = (avgA + 2) % 10  # Change avgB to a value that does not equal avgA
            assert avgA == avgB

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_4():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=2)))
    for nodeA in G.nodes:
        for nodeB in G.neighbors(nodeA):
            avgA = nx.algorithms.assortativity.average_neighbor_degree(G)[nodeA]
            avgB = 0 if avgA != 0 else 1  # Ensure avgB is always different from avgA
            assert avgA == avgB

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_5():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=2)))
    for nodeA in G.nodes:
        for nodeB in G.neighbors(nodeA):
            avgA = nx.algorithms.assortativity.average_neighbor_degree(G)[nodeA]
            avgB = 1000  # Set avgB to a large constant that is unlikely to equal avgA
            assert avgA == avgB