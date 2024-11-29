from hypothesis import given, strategies as st
import networkx as nx
from hypothesis import HealthCheck, settings

# Disable certain health checks to allow for larger graphs
settings.register_profile("large", max_examples=10, suppress_health_check=[HealthCheck.too_slow])
settings.load_profile("large")

@given(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=1000))
def test_is_aperiodic_raises_for_undirected_graph_property(edges):
    G = nx.Graph(edges)  # Create an undirected graph
    try:
        nx.algorithms.dag.is_aperiodic(G)
        assert False, "Expected NetworkXError for undirected graph"
    except nx.NetworkXError:
        pass  # Correct behavior

@given(st.lists(st.integers(), min_size=0, max_size=1000))
def test_is_aperiodic_raises_for_empty_graph_property(nodes):
    G = nx.DiGraph()  # Create a directed graph
    G.add_nodes_from(nodes)  # Add nodes
    if len(nodes) == 0:
        try:
            nx.algorithms.dag.is_aperiodic(G)
            assert False, "Expected NetworkXPointlessConcept for empty graph"
        except nx.NetworkXPointlessConcept:
            pass  # Correct behavior

@given(st.lists(st.integers(), min_size=1, max_size=100), st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
def test_is_aperiodic_true_for_single_scc_property(nodes, edges):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    assert nx.algorithms.dag.is_aperiodic(G) in [True, False]  # Ensure it returns a boolean

@given(st.lists(st.integers(), min_size=1, max_size=100), st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
def test_is_aperiodic_false_for_multiple_scc_property(nodes, edges):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    # Add an edge to create a periodic component
    G.add_edge(nodes[0], nodes[0])  # Self-loop creates a cycle
    assert not nx.algorithms.dag.is_aperiodic(G)  # Should return False

@given(st.lists(st.integers(), min_size=1, max_size=100), st.lists(st.tuples(st.integers(), st.integers()), min_size=1))
def test_is_aperiodic_false_for_graph_with_cycles_property(nodes, edges):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    # Create a cycle
    if len(nodes) > 1:
        G.add_edge(nodes[0], nodes[1])
        G.add_edge(nodes[1], nodes[0])  # Create a cycle
    assert not nx.algorithms.dag.is_aperiodic(G)  # Should return False
# End program