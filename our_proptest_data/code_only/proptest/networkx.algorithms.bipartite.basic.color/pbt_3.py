from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_contains_two_colors_property(data):
    G = data.draw(st.builds(nx.bipartite.random_graph, st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)))
    color_result = nx.algorithms.bipartite.basic.color(G)
    assert set(color_result.values()) == {0, 1}

@given(st.data())
def test_empty_graph_output_property(data):
    G = nx.Graph()  # empty graph
    color_result = nx.algorithms.bipartite.basic.color(G)
    assert color_result == {}

@given(st.data())
def test_isolated_nodes_colored_zero_property(data):
    G = nx.Graph()
    G.add_nodes_from(range(5))  # adding isolated nodes
    color_result = nx.algorithms.bipartite.basic.color(G)
    for node in G.nodes():
        assert color_result[node] == 0

@given(st.data())
def test_one_to_one_mapping_property(data):
    G = data.draw(st.builds(nx.bipartite.random_graph, st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)))
    color_result = nx.algorithms.bipartite.basic.color(G)
    assert len(color_result) == len(G.nodes())

@given(st.data())
def test_not_bipartite_graph_raises_error_property(data):
    G = data.draw(st.builds(nx.generators.random_graphs.erdos_renyi_graph, st.integers(min_value=1, max_value=100), st.floats(min_value=0, max_value=1)))
    if not nx.is_bipartite(G):
        try:
            nx.algorithms.bipartite.basic.color(G)
            assert False, "Expected NetworkXError for non-bipartite graph"
        except nx.NetworkXError:
            pass  # expected error
# End program