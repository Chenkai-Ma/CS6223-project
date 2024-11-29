from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import bipartite

@given(st.data())
def test_output_contains_two_distinct_colors_property(data):
    G = data.draw(st.data().draw(st.one_of(st.graphs(), st.bipartite_graphs())))
    c = bipartite.color(G)
    assert set(c.values()) == {0, 1}

@given(st.data())
def test_output_contains_all_nodes_property(data):
    G = data.draw(st.data().draw(st.one_of(st.graphs(), st.bipartite_graphs())))
    c = bipartite.color(G)
    assert all(node in c for node in G.nodes)

@given(st.data())
def test_adjacent_nodes_have_different_colors_property(data):
    G = data.draw(st.data().draw(st.one_of(st.graphs(), st.bipartite_graphs())))
    c = bipartite.color(G)
    for u, v in G.edges:
        assert c[u] != c[v]

@given(st.data())
def test_non_bipartite_graph_raises_exception_property(data):
    G = data.draw(st.graphs())
    if not nx.is_bipartite(G):
        with pytest.raises(nx.NetworkXError):
            bipartite.color(G)

@given(st.data())
def test_isolated_nodes_colored_zero_property(data):
    G = data.draw(st.data().draw(st.one_of(st.graphs(), st.bipartite_graphs())))
    c = bipartite.color(G)
    for node in nx.isolates(G):
        assert c[node] == 0
# End program