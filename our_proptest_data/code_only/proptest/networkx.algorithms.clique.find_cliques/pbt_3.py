from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.data())
def test_output_nodes_are_in_input_graph_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=20), 
                             p=st.floats(min_value=0, max_value=1)))
    cliques = list(find_cliques(G))
    for clique in cliques:
        assert all(node in G for node in clique)

@given(st.data())
def test_cliques_are_complete_subgraphs_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=20), 
                             p=st.floats(min_value=0, max_value=1)))
    cliques = list(find_cliques(G))
    for clique in cliques:
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                assert G.has_edge(clique[i], clique[j])

@given(st.data())
def test_all_maximal_cliques_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=20), 
                             p=st.floats(min_value=0, max_value=1)))
    cliques = list(find_cliques(G))
    for clique in cliques:
        for node in G.nodes():
            if node not in clique and all(G.has_edge(node, other) for other in clique):
                assert False  # A node that can extend the clique should not exist

@given(st.data())
def test_empty_graph_yields_no_cliques_property(data):
    G = nx.Graph()
    cliques = list(find_cliques(G))
    assert cliques == []

@given(st.data())
def test_given_nodes_form_clique_or_raise_property(data):
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=20), 
                             p=st.floats(min_value=0, max_value=1)))
    nodes = data.draw(st.lists(st.sampled_from(G.nodes()), min_size=1, max_size=5))
    if not all(G.has_edge(nodes[i], nodes[j]) for i in range(len(nodes)) for j in range(i + 1, len(nodes))):
        with pytest.raises(ValueError):
            list(find_cliques(G, nodes))
    else:
        cliques = list(find_cliques(G, nodes))
        assert any(set(nodes).issubset(set(clique)) for clique in cliques)

# End program