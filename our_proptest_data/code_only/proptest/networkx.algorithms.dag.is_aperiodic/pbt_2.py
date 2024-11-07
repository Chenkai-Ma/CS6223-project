from hypothesis import given, strategies as st
import networkx as nx
from networkx import algorithms

@given(st.lists(st.integers(), min_size=1))
def test_is_aperiodic_undirected_graph_property(nodes):
    G = nx.Graph()  # Create an undirected graph
    G.add_nodes_from(nodes)
    with pytest.raises(nx.NetworkXError):
        algorithms.dag.is_aperiodic(G)

@given(st.lists(st.integers(), min_size=0))
def test_is_aperiodic_empty_graph_property(nodes):
    G = nx.DiGraph()  # Create a directed graph
    G.add_nodes_from(nodes)
    if len(nodes) == 0:
        with pytest.raises(nx.NetworkXPointlessConcept):
            algorithms.dag.is_aperiodic(G)

@given(st.lists(st.integers(), min_size=1))
def test_is_aperiodic_single_scc_property(nodes):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from((nodes[i], nodes[(i + 1) % len(nodes)]) for i in range(len(nodes)))  # Create a cycle
    assert algorithms.dag.is_aperiodic(G) is True

@given(st.lists(st.integers(), min_size=2))
def test_is_aperiodic_multiple_scc_property(nodes):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edge(nodes[0], nodes[1])
    G.add_edge(nodes[1], nodes[0])
    G.add_edge(nodes[0], max(nodes) + 1)  # Create a separate component
    assert algorithms.dag.is_aperiodic(G) is False

@given(st.lists(st.integers(), min_size=2))
def test_is_aperiodic_with_cycles_property(nodes):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from((nodes[i], nodes[i]) for i in range(len(nodes)))  # Create self-loops
    assert algorithms.dag.is_aperiodic(G) is False
# End program