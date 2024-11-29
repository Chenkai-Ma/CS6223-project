from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_two_distinct_colors_property(data):
    G = data.draw(st.one_of(st.graphs(directed=False, nodes=st.integers(), edges=st.tuples(st.integers(), st.integers()))))
    try:
        color_result = nx.algorithms.bipartite.color(G)
        assert set(color_result.values()) == {0, 1}
    except nx.NetworkXError:
        pass  # Expected for non-bipartite graphs

@given(st.data())
def test_all_nodes_colored_property(data):
    G = data.draw(st.one_of(st.graphs(directed=False, nodes=st.integers(), edges=st.tuples(st.integers(), st.integers()))))
    try:
        color_result = nx.algorithms.bipartite.color(G)
        assert all(node in color_result for node in G.nodes())
    except nx.NetworkXError:
        pass  # Expected for non-bipartite graphs

@given(st.data())
def test_adjacent_nodes_different_colors_property(data):
    G = data.draw(st.one_of(st.graphs(directed=False, nodes=st.integers(), edges=st.tuples(st.integers(), st.integers()))))
    try:
        color_result = nx.algorithms.bipartite.color(G)
        for u, v in G.edges():
            assert color_result[u] != color_result[v]
    except nx.NetworkXError:
        pass  # Expected for non-bipartite graphs

@given(st.data())
def test_networkx_error_for_non_bipartite_property(data):
    G = data.draw(st.one_of(st.graphs(directed=False, nodes=st.integers(), edges=st.tuples(st.integers(), st.integers(), min_size=1))))
    if not nx.is_bipartite(G):
        with st.raises(nx.NetworkXError):
            nx.algorithms.bipartite.color(G)

@given(st.data())
def test_isolated_nodes_colored_zero_property(data):
    G = data.draw(st.one_of(st.graphs(directed=False, nodes=st.integers(), edges=st.tuples(st.integers(), st.integers()))))
    try:
        color_result = nx.algorithms.bipartite.color(G)
        isolates = list(nx.isolates(G))
        assert all(color_result[node] == 0 for node in isolates)
    except nx.NetworkXError:
        pass  # Expected for non-bipartite graphs
# End program