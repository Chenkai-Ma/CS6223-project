from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_is_non_negative_property(data):
    G = data.draw(st.one_of(st.lists(st.integers()), st.sets(st.integers())))
    if G:
        graph = nx.Graph(G)
        result = nx.algorithms.approximation.clique.large_clique_size(graph)
        assert result >= 0

@given(st.data())
def test_output_does_not_exceed_node_count_property(data):
    G = data.draw(st.one_of(st.lists(st.integers()), st.sets(st.integers())))
    graph = nx.Graph(G)
    result = nx.algorithms.approximation.clique.large_clique_size(graph)
    assert result <= graph.number_of_nodes()

@given(st.data())
def test_empty_graph_returns_zero_property(data):
    G = []
    graph = nx.Graph(G)
    result = nx.algorithms.approximation.clique.large_clique_size(graph)
    assert result == 0

@given(st.data())
def test_output_with_max_degree_property(data):
    G = data.draw(st.sets(st.integers()))
    graph = nx.Graph(G)
    for node in graph.nodes:
        graph.add_edges_from([(node, neighbor) for neighbor in graph.nodes if neighbor != node])
    result = nx.algorithms.approximation.clique.large_clique_size(graph)
    max_degree = max(dict(graph.degree).values(), default=0)
    assert result <= max_degree + 1

@given(st.data())
def test_output_zero_for_isolated_nodes_property(data):
    G = data.draw(st.sets(st.integers()))
    graph = nx.Graph(G)
    for node in graph.nodes:
        graph.add_node(node)
    result = nx.algorithms.approximation.clique.large_clique_size(graph)
    assert result == 0
# End program