from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.data())
def test_output_nodes_are_subsets_property(data):
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    for clique in cliques:
        assert set(clique).issubset(graph.nodes)

@given(st.data())
def test_cliques_are_complete_subgraphs_property(data):
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    for clique in cliques:
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                assert graph.has_edge(clique[i], clique[j])

@given(st.data())
def test_cliques_are_maximal_property(data):
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    for clique in cliques:
        # Check that no nodes can be added to the clique without breaking its completeness
        for node in graph.nodes:
            if node not in clique and graph.has_edges_from((node, n) for n in clique):
                assert False  # A node can be added to the clique

@given(st.data())
def test_empty_graph_yields_no_cliques_property(data):
    graph = nx.Graph()
    cliques = list(find_cliques(graph))
    assert cliques == []

@given(st.data())
def test_specific_nodes_must_form_clique_property(data):
    nodes = data.draw(st.sets(st.integers(), min_size=2, max_size=10))
    graph = nx.complete_graph(nodes)  # Create a complete graph
    cliques = list(find_cliques(graph, nodes=list(nodes)))
    assert len(cliques) > 0  # There must be at least one clique, the nodes themselves
    for clique in cliques:
        assert set(clique) == set(nodes)  # Must yield the specified clique
# End program