# property to violate: The average neighbor degree for a node should be equal to the total degree of its neighbors divided by the node's degree, ensuring that the calculation correctly reflects the average.
from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_1(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    for node in G.nodes:
        avg = nx.algorithms.assortativity.average_neighbor_degree(G)[node]
        neighbors = list(G.neighbors(node))
        if len(neighbors) > 0:
            total_degree = sum(G.degree[nbr] for nbr in neighbors)
            assert avg != total_degree / G.degree[node]  # Violation: output is made unequal

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_2(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    for node in G.nodes:
        avg = nx.algorithms.assortativity.average_neighbor_degree(G)[node]
        neighbors = list(G.neighbors(node))
        if len(neighbors) > 0:
            total_degree = sum(G.degree[nbr] for nbr in neighbors)
            assert avg != (total_degree / G.degree[node]) + 1  # Violation: output is offset by +1

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_3(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    for node in G.nodes:
        avg = nx.algorithms.assortativity.average_neighbor_degree(G)[node]
        neighbors = list(G.neighbors(node))
        if len(neighbors) > 0:
            total_degree = sum(G.degree[nbr] for nbr in neighbors)
            assert avg != total_degree / (G.degree[node] + 1)  # Violation: denominator is increased by 1

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_4(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    for node in G.nodes:
        avg = nx.algorithms.assortativity.average_neighbor_degree(G)[node]
        neighbors = list(G.neighbors(node))
        if len(neighbors) > 0:
            total_degree = sum(G.degree[nbr] for nbr in neighbors)
            assert avg != total_degree * 2 / G.degree[node]  # Violation: output is doubled

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_5(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    for node in G.nodes:
        avg = nx.algorithms.assortativity.average_neighbor_degree(G)[node]
        neighbors = list(G.neighbors(node))
        if len(neighbors) > 0:
            total_degree = sum(G.degree[nbr] for nbr in neighbors)
            assert avg != (total_degree / G.degree[node]) * 0.5  # Violation: output is halved