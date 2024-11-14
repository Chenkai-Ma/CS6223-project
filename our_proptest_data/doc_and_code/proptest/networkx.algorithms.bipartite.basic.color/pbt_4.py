from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import bipartite

@given(st.data())
def test_output_contains_two_distinct_colors_property(data):
    # Generate a bipartite graph
    G = data.draw(st.builds(nx.bipartite.random_graph, st.integers(min_value=1, max_value=100), 
                             st.integers(min_value=1, max_value=100)))
    color = bipartite.color(G)
    assert set(color.values()) == {0, 1}

@given(st.data())
def test_output_contains_all_nodes_property(data):
    # Generate a bipartite graph
    G = data.draw(st.builds(nx.bipartite.random_graph, st.integers(min_value=1, max_value=100), 
                             st.integers(min_value=1, max_value=100)))
    color = bipartite.color(G)
    assert all(node in color for node in G.nodes)

@given(st.data())
def test_adjacent_nodes_have_different_colors_property(data):
    # Generate a bipartite graph
    G = data.draw(st.builds(nx.bipartite.random_graph, st.integers(min_value=1, max_value=100), 
                             st.integers(min_value=1, max_value=100)))
    color = bipartite.color(G)
    for u, v in G.edges:
        assert color[u] != color[v]

@given(st.data())
def test_non_bipartite_graph_raises_exception_property(data):
    # Generate a non-bipartite graph
    G = data.draw(st.builds(nx.complete_graph, st.integers(min_value=3, max_value=10)))
    try:
        bipartite.color(G)
        assert False, "Expected NetworkXError for non-bipartite graph"
    except nx.NetworkXError:
        pass  # Expected behavior

@given(st.data())
def test_isolated_nodes_colored_zero_property(data):
    # Generate a bipartite graph with isolated nodes
    G = data.draw(st.builds(nx.bipartite.random_graph, st.integers(min_value=1, max_value=100), 
                             st.integers(min_value=1, max_value=100)))
    # Add isolated nodes
    for _ in range(10):
        G.add_node(G.number_of_nodes())
    color = bipartite.color(G)
    assert all(color[node] == 0 for node in nx.isolates(G))

# End program