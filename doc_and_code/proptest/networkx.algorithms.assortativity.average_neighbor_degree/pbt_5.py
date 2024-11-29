from hypothesis import given, strategies as st
import networkx as nx

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), st.sampled_from(['in', 'out', 'in+out']))
def test_output_contains_all_nodes_property(data, source):
    G = nx.Graph(data)
    avg_neighbor_deg = nx.average_neighbor_degree(G, source=source)
    assert all(node in avg_neighbor_deg for node in G.nodes)

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), st.sampled_from(['in', 'out', 'in+out']))
def test_average_neighbor_degree_non_negative_property(data, source):
    G = nx.Graph(data)
    avg_neighbor_deg = nx.average_neighbor_degree(G, source=source)
    assert all(value >= 0 for value in avg_neighbor_deg.values())

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), st.sampled_from(['in', 'out', 'in+out']))
def test_degree_zero_average_property(data, source):
    G = nx.Graph(data)
    avg_neighbor_deg = nx.average_neighbor_degree(G, source=source)
    for node in G.nodes:
        if G.degree(node) == 0:
            assert avg_neighbor_deg[node] == 0.0

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), st.sampled_from(['in', 'out', 'in+out']))
def test_average_neighbor_degree_correctness_property(data, source):
    G = nx.Graph(data)
    avg_neighbor_deg = nx.average_neighbor_degree(G, source=source)

    for node in G.nodes:
        neighbors = list(G.neighbors(node))
        if len(neighbors) > 0:
            total_degree = sum(G.degree(n) for n in neighbors)
            assert avg_neighbor_deg[node] == total_degree / len(neighbors)

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100), st.sampled_from(['in', 'out', 'in+out']))
def test_output_stability_property(data, source):
    G = nx.Graph(data)
    avg_neighbor_deg_first = nx.average_neighbor_degree(G, source=source)
    avg_neighbor_deg_second = nx.average_neighbor_degree(G, source=source)
    assert avg_neighbor_deg_first == avg_neighbor_deg_second
# End program