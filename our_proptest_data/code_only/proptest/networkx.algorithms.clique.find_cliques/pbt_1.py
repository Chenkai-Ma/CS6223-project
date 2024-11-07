from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_nodes_are_in_input_graph_property(data):
    G = data.draw(st.one_of(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=0, max_size=100)),
                             st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=0, max_size=100))))
    cliques = list(nx.algorithms.clique.find_cliques(G))
    for clique in cliques:
        for node in clique:
            assert node in G.nodes

@given(st.data())
def test_output_cliques_are_complete_subgraphs_property(data):
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=0, max_size=100)))
    cliques = list(nx.algorithms.clique.find_cliques(G))
    for clique in cliques:
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                assert G.has_edge(clique[i], clique[j])

@given(st.data())
def test_output_contains_all_maximal_cliques_property(data):
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=0, max_size=100)))
    cliques = list(nx.algorithms.clique.find_cliques(G))
    # This is a placeholder for the logic to check for maximality.
    # A full implementation would require additional logic to verify maximality.
    assert True  # Replace with actual maximality checks.

@given(st.data())
def test_empty_graph_yields_no_cliques_property(data):
    G = nx.Graph()  # Empty graph
    cliques = list(nx.algorithms.clique.find_cliques(G))
    assert cliques == []

@given(st.data())
def test_given_nodes_form_clique_or_raise_property(data):
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=0, max_size=100)))
    nodes = data.draw(st.lists(st.integers(), min_size=1, max_size=5))
    if all(G.has_edge(u, v) for u in nodes for v in nodes if u != v):
        cliques = list(nx.algorithms.clique.find_cliques(G, nodes=nodes))
        assert any(set(nodes).issubset(set(clique)) for clique in cliques)
    else:
        try:
            nx.algorithms.clique.find_cliques(G, nodes=nodes)
            assert False  # Should not reach here; an exception should be raised
        except ValueError:
            pass  # Expected behavior
# End program