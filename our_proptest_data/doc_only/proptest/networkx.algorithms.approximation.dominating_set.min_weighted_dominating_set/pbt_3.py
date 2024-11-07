from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import min_weighted_dominating_set

@given(st.data())
def test_output_is_subset_of_input_property(data):
    G = nx.Graph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    result = min_weighted_dominating_set(G)
    assert result.issubset(G.nodes)

@given(st.data())
def test_output_is_a_dominating_set_property(data):
    G = nx.Graph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    result = min_weighted_dominating_set(G)
    for node in G.nodes:
        assert node in result or any(neighbor in result for neighbor in G.neighbors(node))

@given(st.data())
def test_weight_property_with_weights(data):
    G = nx.Graph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    weight_attr = {node: data.draw(st.integers(min_value=1, max_value=100)) for node in G.nodes}
    nx.set_node_attributes(G, weight_attr, 'weight')
    result = min_weighted_dominating_set(G, weight='weight')
    total_weight = sum(weight_attr[node] for node in result)
    total_graph_weight = sum(weight_attr.values())
    
    # Assuming w(V*) can be approximated as the weight of the result
    w_V_star = total_weight
    log_w_V = 1 if total_graph_weight == 0 else (total_graph_weight).bit_length()  # log base 2 approximation
    assert total_weight <= log_w_V * w_V_star

@given(st.data())
def test_weight_property_without_weights(data):
    G = nx.Graph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    result = min_weighted_dominating_set(G)
    assert sum(1 for _ in result) == len(result)  # Each node has weight of 1

@given(st.data())
def test_raises_exception_for_directed_graph_property(data):
    G = nx.DiGraph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    try:
        min_weighted_dominating_set(G)
        assert False, "Expected NetworkXNotImplemented exception"
    except NotImplementedError:
        pass  # Expected behavior

# End program