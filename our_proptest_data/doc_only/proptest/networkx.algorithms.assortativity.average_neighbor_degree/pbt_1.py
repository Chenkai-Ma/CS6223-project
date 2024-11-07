from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.assortativity import average_neighbor_degree

@given(st.data())
def test_output_contains_all_nodes_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    nodes = list(G.nodes())
    output = average_neighbor_degree(G)
    assert all(node in output for node in nodes)

@given(st.data())
def test_average_degree_non_negative_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G)
    assert all(degree >= 0 for degree in output.values())

@given(st.data())
def test_average_degree_symmetric_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=2, max_size=10)))
    output = average_neighbor_degree(G)
    for u, v in G.edges():
        assert output[u] == output[v] if u in G.neighbors(v) else True

@given(st.data())
def test_in_neighbors_average_degree_zero_property(data):
    G = data.draw(st.builds(nx.DiGraph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output = average_neighbor_degree(G, source='in')
    for node in G.nodes():
        if len(list(G.predecessors(node))) == 0:
            assert output[node] == 0

@given(st.data())
def test_consistency_of_output_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1, max_size=10)))
    output1 = average_neighbor_degree(G)
    output2 = average_neighbor_degree(G)
    assert output1 == output2
# End program