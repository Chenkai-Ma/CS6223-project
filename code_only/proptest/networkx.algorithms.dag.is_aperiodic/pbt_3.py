from hypothesis import given, strategies as st
import networkx as nx

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=100))
def test_is_aperiodic_raises_for_undirected_graph_property(edges):
    G = nx.Graph(edges)
    with pytest.raises(nx.NetworkXError):
        nx.algorithms.dag.is_aperiodic(G)

@given(st.lists(st.integers(), min_size=0, max_size=100))
def test_is_aperiodic_raises_for_empty_graph_property(nodes):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    if len(nodes) == 0:
        with pytest.raises(nx.NetworkXPointlessConcept):
            nx.algorithms.dag.is_aperiodic(G)

@given(st.lists(st.integers(), min_size=1, max_size=100))
def test_is_aperiodic_returns_true_for_single_scc_property(nodes):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    for i in range(len(nodes) - 1):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[-1], nodes[0])  # create a cycle
    assert nx.algorithms.dag.is_aperiodic(G) == True

@given(st.lists(st.integers(), min_size=1, max_size=100))
def test_is_aperiodic_returns_false_for_multiple_scc_property(nodes):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    for i in range(len(nodes) - 1):
        G.add_edge(nodes[i], nodes[i + 1])
    G.add_edge(nodes[-1], nodes[0])  # create a cycle
    G.add_edge(nodes[0], nodes[-1])  # introduce another edge to create a second component
    assert nx.algorithms.dag.is_aperiodic(G) == False

@given(st.lists(st.integers(), min_size=1, max_size=100))
def test_is_aperiodic_returns_false_for_graph_with_cycles_property(nodes):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    for i in range(len(nodes)):
        G.add_edge(nodes[i], nodes[i])  # create self-loops
    assert nx.algorithms.dag.is_aperiodic(G) == False
# End program