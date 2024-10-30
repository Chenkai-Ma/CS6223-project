from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.assortativity import average_neighbor_degree

@given(st.data())
def test_output_contains_all_nodes_property(data):
    G = data.draw(st.one_of(st.builds(nx.Graph), st.builds(nx.DiGraph)))
    nodes = list(G.nodes)
    output = average_neighbor_degree(G)
    assert all(node in output for node in nodes)

@given(st.data())
def test_average_degree_non_negative_property(data):
    G = data.draw(st.one_of(st.builds(nx.Graph), st.builds(nx.DiGraph)))
    output = average_neighbor_degree(G)
    assert all(value >= 0 for value in output.values())

@given(st.data())
def test_average_degree_symmetry_property(data):
    G = data.draw(st.builds(nx.Graph))
    if G.number_of_edges() > 0:
        output = average_neighbor_degree(G)
        for node in G.nodes:
            for neighbor in G.neighbors(node):
                assert output[node] == output[neighbor]

@given(st.data())
def test_average_degree_zero_for_no_predecessors_property(data):
    G = nx.DiGraph()
    G.add_nodes_from(range(5))
    output = average_neighbor_degree(G, source='in')
    for node in G.nodes:
        if G.in_degree(node) == 0:
            assert output[node] == 0.0

@given(st.data())
def test_consistent_output_property(data):
    G = data.draw(st.one_of(st.builds(nx.Graph), st.builds(nx.DiGraph)))
    params = {
        'source': data.draw(st.sampled_from(['in', 'out', 'in+out'])),
        'target': data.draw(st.sampled_from(['in', 'out', 'in+out'])),
    }
    output1 = average_neighbor_degree(G, **params)
    output2 = average_neighbor_degree(G, **params)
    assert output1 == output2
# End program