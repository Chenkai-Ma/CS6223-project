from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.dag import is_aperiodic

@given(st.data())
def test_is_aperiodic_undirected_graph_property(data):
    G = nx.Graph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    with pytest.raises(nx.NetworkXError):
        is_aperiodic(G)

@given(st.data())
def test_is_aperiodic_empty_graph_property(data):
    G = nx.DiGraph()
    with pytest.raises(nx.NetworkXPointlessConcept):
        is_aperiodic(G)

@given(st.data())
def test_is_aperiodic_single_scc_property(data):
    G = nx.DiGraph()
    nodes = data.draw(st.lists(st.integers(), min_size=1))
    G.add_nodes_from(nodes)
    G.add_edges_from(data.draw(st.lists(st.tuples(st.sampled_from(nodes), st.sampled_from(nodes)), min_size=1)))
    assert is_aperiodic(G) == True  # Assuming this specific input is aperiodic

@given(st.data())
def test_is_aperiodic_multiple_scc_property(data):
    G = nx.DiGraph()
    nodes = data.draw(st.lists(st.integers(), min_size=1))
    G.add_nodes_from(nodes)
    G.add_edges_from(data.draw(st.lists(st.tuples(st.sampled_from(nodes), st.sampled_from(nodes)), min_size=1)))
    # Manually create a periodic component
    G.add_edge(nodes[0], nodes[0])  # Adding a self-loop
    assert is_aperiodic(G) == False

@given(st.data())
def test_is_aperiodic_graph_with_cycles_property(data):
    G = nx.DiGraph()
    nodes = data.draw(st.lists(st.integers(), min_size=1))
    G.add_nodes_from(nodes)
    edges = data.draw(st.lists(st.tuples(st.sampled_from(nodes), st.sampled_from(nodes)), min_size=1))
    G.add_edges_from(edges)
    # Ensure at least one cycle
    G.add_edge(nodes[0], nodes[0])
    assert is_aperiodic(G) == False

# End program