from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import bipartite
from networkx.exception import NetworkXError

@given(st.data())
def test_output_length_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.path_graph, st.integers(min_value=1, max_value=1000)),
        st.builds(nx.complete_bipartite_graph, st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100))
    ))
    c = bipartite.color(G)
    assert len(c) == G.number_of_nodes()

@given(st.data())
def test_color_values_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.path_graph, st.integers(min_value=1, max_value=1000)),
        st.builds(nx.complete_bipartite_graph, st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100))
    ))
    c = bipartite.color(G)
    assert all(color in {0, 1} for color in c.values())

@given(st.data())
def test_edges_different_colors_property(data):
    G = data.draw(st.builds(nx.complete_bipartite_graph, st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)))
    c = bipartite.color(G)
    for u, v in G.edges():
        assert c[u] != c[v]

@given(st.data())
def test_bipartite_coloring_property(data):
    G = data.draw(st.one_of(
        st.builds(nx.complete_bipartite_graph, st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)),
        st.builds(nx.path_graph, st.integers(min_value=1, max_value=1000))
    ))
    c = bipartite.color(G)
    for u, v in G.edges():
        assert c[u] != c[v]

@given(st.data())
def test_non_bipartite_graph_raises_error_property(data):
    G = data.draw(st.builds(nx.complete_graph, st.integers(min_value=3, max_value=100)))
    try:
        bipartite.color(G)
        assert False, "Expected NetworkXError for non-bipartite graph"
    except NetworkXError:
        pass
# End program