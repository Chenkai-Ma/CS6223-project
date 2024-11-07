# property to violate: If the graph is directed and the source is set to "in", the average neighbor degree for nodes with no predecessors should be zero.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.assortativity import average_neighbor_degree

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_1():
    G = data.draw(st.builds(nx.DiGraph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G, source='in')
    for node in G.nodes():
        if len(list(G.predecessors(node))) == 0:
            output[node] = 1  # Violating the property by setting it to 1 instead of 0
            assert output[node] == 0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_2():
    G = data.draw(st.builds(nx.DiGraph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G, source='in')
    for node in G.nodes():
        if len(list(G.predecessors(node))) == 0:
            output[node] = -1  # Violating the property by setting it to -1 instead of 0
            assert output[node] == 0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_3():
    G = data.draw(st.builds(nx.DiGraph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G, source='in')
    for node in G.nodes():
        if len(list(G.predecessors(node))) == 0:
            output[node] = 10  # Violating the property by setting it to 10 instead of 0
            assert output[node] == 0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_4():
    G = data.draw(st.builds(nx.DiGraph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G, source='in')
    for node in G.nodes():
        if len(list(G.predecessors(node))) == 0:
            output[node] = 0.5  # Violating the property by setting it to 0.5 instead of 0
            assert output[node] == 0

@given(st.data())
def test_violation_of_networkx_algorithms_assortativity_average_neighbor_degree_5():
    G = data.draw(st.builds(nx.DiGraph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G, source='in')
    for node in G.nodes():
        if len(list(G.predecessors(node))) == 0:
            output[node] = 100  # Violating the property by setting it to 100 instead of 0
            assert output[node] == 0