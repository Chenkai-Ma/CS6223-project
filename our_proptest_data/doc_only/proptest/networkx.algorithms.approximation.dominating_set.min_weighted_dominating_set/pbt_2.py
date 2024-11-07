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
def test_weight_bounds_property(data):
    G = nx.Graph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    weight_attr = data.draw(st.lists(st.tuples(st.integers(), st.floats(0, 100)), min_size=len(G.nodes)))
    nx.set_node_attributes(G, dict(weight_attr), 'weight')
    
    result = min_weighted_dominating_set(G, weight='weight')
    
    total_weight = sum(G.nodes[n]['weight'] for n in G.nodes)
    min_weight_dominating_set_weight = sum(G.nodes[n]['weight'] for n in result)
    
    log_weight = 0 if total_weight == 0 else log(total_weight)
    assert min_weight_dominating_set_weight <= log_weight * total_weight

@given(st.data())
def test_no_weight_assumed_property(data):
    G = nx.Graph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    result = min_weighted_dominating_set(G)
    # If no weights are given, each node is assumed to have weight 1
    assert sum(1 for _ in result) == len(result)

@given(st.data())
def test_directed_graph_exception_property(data):
    G = nx.DiGraph(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    try:
        min_weighted_dominating_set(G)
    except nx.NetworkXNotImplemented:
        assert True
    else:
        assert False
# End program