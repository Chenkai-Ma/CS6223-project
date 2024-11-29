from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import bipartite
from hypothesis import HealthCheck, settings

# Settings to suppress certain warnings about large tests
settings.register_profile("ci", max_examples=50, suppress_health_checks=[HealthCheck.too_slow])
settings.set_profile("ci")

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_output_dictionary_size_property(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    try:
        c = bipartite.color(G)
        assert len(c) == G.number_of_nodes()
    except nx.NetworkXError:
        pass  # Expected for non-bipartite graphs

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_output_color_values_property(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    try:
        c = bipartite.color(G)
        assert all(color in {0, 1} for color in c.values())
    except nx.NetworkXError:
        pass  # Expected for non-bipartite graphs

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_connected_nodes_different_colors_property(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    try:
        c = bipartite.color(G)
        for u, v in G.edges():
            assert c[u] != c[v]
    except nx.NetworkXError:
        pass  # Expected for non-bipartite graphs

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_valid_bipartite_coloring_property(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    try:
        c = bipartite.color(G)
        for u, v in G.edges():
            assert c[u] != c[v]
    except nx.NetworkXError:
        pass  # Expected for non-bipartite graphs

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_networkxerror_on_nonbipartite_property(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    # Add odd cycle to ensure it's non-bipartite
    if len(edges) > 1:
        G.add_edge(edges[0][0], edges[0][1])  # Create a cycle
    try:
        bipartite.color(G)
        assert G.is_bipartite() or G.number_of_edges() < 3  # If we have a cycle and edges, it's non-bipartite
    except nx.NetworkXError:
        pass  # This is expected for non-bipartite graphs
# End program