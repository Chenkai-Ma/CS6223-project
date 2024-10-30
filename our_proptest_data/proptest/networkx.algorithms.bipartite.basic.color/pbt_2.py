from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import bipartite

@given(st.data())
def test_output_length_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        assert len(c) == len(G.nodes)

@given(st.data())
def test_color_value_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        for color in c.values():
            assert color in {0, 1}

@given(st.data())
def test_adjacent_nodes_diff_color_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        for u, v in G.edges:
            assert c[u] != c[v]

@given(st.data())
def test_bipartite_coloring_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        for u, v in G.edges:
            assert c[u] != c[v]

@given(st.data())
def test_non_bipartite_graph_error_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=3), edges=st.lists(st.tuples(st.integers(), st.integers()))))
    if not bipartite.is_bipartite(G):
        try:
            bipartite.color(G)
            assert False, "Expected NetworkXError for non-bipartite graph"
        except nx.NetworkXError:
            pass

# End program