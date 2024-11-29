from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_contains_two_distinct_colors_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.complete_bipartite_graph, st.integers(min_value=1, max_value=10), st.integers(min_value=1, max_value=10)),
        st.builds(nx.empty_graph, st.integers(min_value=0, max_value=10)),
    ))
    color = nx.algorithms.bipartite.basic.color(G)
    assert set(color.values()) <= {0, 1}

@given(st.data())
def test_empty_graph_output_property(data):
    G = nx.empty_graph()
    color = nx.algorithms.bipartite.basic.color(G)
    assert color == {}

@given(st.data())
def test_isolated_nodes_color_property(data):
    isolated_node_count = data.draw(st.integers(min_value=1, max_value=10))
    G = nx.Graph()
    G.add_nodes_from(range(isolated_node_count))  # Add isolated nodes
    color = nx.algorithms.bipartite.basic.color(G)
    assert all(color[node] == 0 for node in G.nodes())

@given(st.data())
def test_one_to_one_mapping_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.complete_bipartite_graph, st.integers(min_value=1, max_value=10), st.integers(min_value=1, max_value=10)),
        st.builds(nx.empty_graph, st.integers(min_value=0, max_value=10)),
    ))
    color = nx.algorithms.bipartite.basic.color(G)
    assert len(color) == G.number_of_nodes()

@given(st.data())
def test_non_bipartite_graph_error_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.complete_graph, st.integers(min_value=3, max_value=10)),
        st.builds(nx.cycle_graph, st.integers(min_value=4, max_value=10), directed=False)
    ))
    try:
        nx.algorithms.bipartite.basic.color(G)
        assert False  # Should raise an error
    except nx.NetworkXError:
        pass  # Expected behavior

# End program