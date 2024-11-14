from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import bipartite

@given(st.data())
def test_output_contains_two_distinct_keys_property(data):
    G = data.draw(st.builds(nx.bipartite.random_graph, st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)))
    c = bipartite.color(G)
    assert set(c.values()) == {0, 1}

@given(st.data())
def test_output_contains_all_nodes_property(data):
    G = data.draw(st.builds(nx.bipartite.random_graph, st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)))
    c = bipartite.color(G)
    assert all(node in c for node in G.nodes)

@given(st.data())
def test_adjacent_nodes_have_different_colors_property(data):
    G = data.draw(st.builds(nx.bipartite.random_graph, st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)))
    c = bipartite.color(G)
    for u, v in G.edges:
        assert c[u] != c[v]

@given(st.data())
def test_non_bipartite_graph_raises_error_property(data):
    G = data.draw(st.builds(nx.complete_graph, st.integers(min_value=3, max_value=10)))  # Complete graph is not bipartite
    try:
        bipartite.color(G)
        assert False, "Expected NetworkXError for non-bipartite graph."
    except nx.NetworkXError:
        pass  # Test passes if error is raised

@given(st.data())
def test_isolated_nodes_colored_zero_property(data):
    G = data.draw(st.builds(nx.bipartite.random_graph, st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)))
    G.add_node("isolate")  # Adding an isolated node
    c = bipartite.color(G)
    assert c.get("isolate") == 0

# End program