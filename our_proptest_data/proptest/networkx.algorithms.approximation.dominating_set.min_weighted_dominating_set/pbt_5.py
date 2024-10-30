from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import min_weighted_dominating_set

@given(st.data())
def test_output_is_subset_of_nodes_property(data):
    G = nx.Graph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    result = min_weighted_dominating_set(G)
    assert result.issubset(G.nodes)

@given(st.data())
def test_output_is_dominating_set_property(data):
    G = nx.Graph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    result = min_weighted_dominating_set(G)
    for node in G.nodes:
        assert node in result or any(neighbor in result for neighbor in G.neighbors(node))

@given(st.data())
def test_weight_bound_property(data):
    G = nx.Graph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    weights = data.draw(st.dictionaries(st.integers(), st.floats(min_value=0, max_value=100)))
    nx.set_node_attributes(G, weights, 'weight')
    result = min_weighted_dominating_set(G)
    
    total_weight = sum(weights[node] for node in G.nodes)
    min_weight_dominating_set_weight = sum(weights[node] for node in result)
    
    log_w_v = 0 if total_weight == 0 else np.log(total_weight)
    assert min_weight_dominating_set_weight <= log_w_v * min_weight_dominating_set_weight

@given(st.data())
def test_no_weight_assumed_weight_property(data):
    G = nx.Graph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    result = min_weighted_dominating_set(G)
    assert sum(1 for _ in result) == len(result)  # Each node has weight of 1

@given(st.data())
def test_raises_not_implemented_for_directed_graph_property(data):
    G = nx.DiGraph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    try:
        min_weighted_dominating_set(G)
        assert False, "Expected NetworkXNotImplemented exception"
    except nx.NetworkXNotImplemented:
        pass
# End program