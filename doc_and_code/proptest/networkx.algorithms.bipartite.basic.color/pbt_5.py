from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import bipartite

@given(st.data())
def test_color_output_contains_two_distinct_colors_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        assert set(c.values()) == {0, 1}

@given(st.data())
def test_color_output_contains_all_nodes_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        assert all(node in c for node in G.nodes)

@given(st.data())
def test_color_adjacent_nodes_have_different_colors_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        for u, v in G.edges:
            assert c[u] != c[v]

@given(st.data())
def test_color_raises_exception_on_non_bipartite_graph_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if not nx.is_bipartite(G):
        try:
            bipartite.color(G)
            assert False, "Expected NetworkXError for non-bipartite graph."
        except nx.NetworkXError:
            pass

@given(st.data())
def test_color_isolates_colored_zero_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        for node in nx.isolates(G):
            assert c[node] == 0
# End program