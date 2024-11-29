from hypothesis import given, strategies as st
import networkx as nx

# Property 1: The average neighbor degree for any node should be non-negative.
@given(st.lists(st.tuples(st.integers(min_value=0), st.integers(min_value=0)), min_size=1))
def test_average_neighbor_degree_non_negative_property(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    avg_neighbor_deg = nx.algorithms.assortativity.average_neighbor_degree(G)
    for deg in avg_neighbor_deg.values():
        assert deg >= 0

# Property 2: If a node has a degree of zero, its average neighbor degree should be exactly zero.
@given(st.lists(st.tuples(st.integers(min_value=0), st.integers(min_value=0)), min_size=1),
                st.integers(min_value=0, max_value=10))
def test_average_neighbor_degree_zero_degree_property(edges, isolated_node):
    G = nx.Graph()
    G.add_edges_from(edges)
    G.add_node(isolated_node)
    avg_neighbor_deg = nx.algorithms.assortativity.average_neighbor_degree(G)
    assert avg_neighbor_deg[isolated_node] == 0.0

# Property 3: The average neighbor degree should equal the total degree of its neighbors divided by the node's degree.
@given(st.lists(st.tuples(st.integers(min_value=0), st.integers(min_value=0)), min_size=1))
def test_average_neighbor_degree_correctness_property(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    avg_neighbor_deg = nx.algorithms.assortativity.average_neighbor_degree(G)

    for node in G.nodes():
        if G.degree(node) > 0:
            neighbor_degrees = [G.degree(neighbor) for neighbor in G.neighbors(node)]
            expected_avg = sum(neighbor_degrees) / G.degree(node)
            assert avg_neighbor_deg[node] == expected_avg

# Property 4: In an undirected graph, the average neighbor degree should be symmetric.
@given(st.lists(st.tuples(st.integers(min_value=0), st.integers(min_value=0)), min_size=1))
def test_average_neighbor_degree_symmetry_property(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    avg_neighbor_deg = nx.algorithms.assortativity.average_neighbor_degree(G)

    for node in G.nodes():
        for neighbor in G.neighbors(node):
            assert avg_neighbor_deg[node] == avg_neighbor_deg[neighbor]

# Property 5: The average neighbor degree should be invariant under the addition of nodes with no edges.
@given(st.lists(st.tuples(st.integers(min_value=0), st.integers(min_value=0)), min_size=1),
                st.integers(min_value=0, max_value=10))
def test_average_neighbor_degree_invariance_property(edges, isolated_node):
    G = nx.Graph()
    G.add_edges_from(edges)
    avg_neighbor_deg_before = nx.algorithms.assortativity.average_neighbor_degree(G)

    G.add_node(isolated_node)
    avg_neighbor_deg_after = nx.algorithms.assortativity.average_neighbor_degree(G)

    for node in G.nodes():
        assert avg_neighbor_deg_before[node] == avg_neighbor_deg_after[node]

# End program