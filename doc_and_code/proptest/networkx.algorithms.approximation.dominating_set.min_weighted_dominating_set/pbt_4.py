from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import min_weighted_dominating_set

@given(st.data())
def test_output_is_subset_of_input_property(data):
    # Generate a random undirected graph with nodes and weights
    G = nx.random_graphs.erdos_renyi_graph(data.draw(st.integers(min_value=1, max_value=100)), 
                                             data.draw(st.floats(min_value=0, max_value=1)).round(2))
    weights = {node: data.draw(st.floats(min_value=0, max_value=10).filter(lambda x: x >= 0)) for node in G.nodes()}
    nx.set_node_attributes(G, weights, 'weight')

    dom_set = min_weighted_dominating_set(G, weight='weight')
    
    assert dom_set.issubset(G.nodes)

@given(st.data())
def test_output_covers_all_vertices_property(data):
    G = nx.random_graphs.erdos_renyi_graph(data.draw(st.integers(min_value=1, max_value=100)), 
                                             data.draw(st.floats(min_value=0, max_value=1)).round(2))
    weights = {node: data.draw(st.floats(min_value=0, max_value=10).filter(lambda x: x >= 0)) for node in G.nodes()}
    nx.set_node_attributes(G, weights, 'weight')

    dom_set = min_weighted_dominating_set(G, weight='weight')
    
    covered_vertices = set()
    for node in dom_set:
        covered_vertices.add(node)
        covered_vertices.update(G.neighbors(node))
    
    assert covered_vertices == set(G.nodes)

@given(st.data())
def test_output_weight_limit_property(data):
    G = nx.random_graphs.erdos_renyi_graph(data.draw(st.integers(min_value=1, max_value=100)), 
                                             data.draw(st.floats(min_value=0, max_value=1)).round(2))
    weights = {node: data.draw(st.floats(min_value=0, max_value=10).filter(lambda x: x >= 0)) for node in G.nodes()}
    nx.set_node_attributes(G, weights, 'weight')

    dom_set = min_weighted_dominating_set(G, weight='weight')

    total_weight = sum(G.nodes[node].get('weight', 1) for node in dom_set)
    total_graph_weight = sum(weights.values())
    min_weight_dominating_set_weight = sum(weights[node] for node in min_weighted_dominating_set(G, weight='weight'))

    log_w_V = 0 if total_graph_weight == 0 else np.log(total_graph_weight)
    assert total_weight <= log_w_V * min_weight_dominating_set_weight

@given(st.data())
def test_empty_graph_output_property(data):
    G = nx.Graph()  # Create an empty graph
    dom_set = min_weighted_dominating_set(G)
    
    assert dom_set == set()

@given(st.data())
def test_output_stability_property(data):
    G = nx.random_graphs.erdos_renyi_graph(data.draw(st.integers(min_value=1, max_value=100)), 
                                             data.draw(st.floats(min_value=0, max_value=1)).round(2))
    weights = {node: data.draw(st.floats(min_value=0, max_value=10).filter(lambda x: x >= 0)) for node in G.nodes()}
    nx.set_node_attributes(G, weights, 'weight')

    original_dom_set = min_weighted_dominating_set(G, weight='weight')
    
    # Modify the graph slightly
    if len(G.nodes) > 0:
        G.add_node(max(G.nodes)+1)  # Add a new node
    new_dom_set = min_weighted_dominating_set(G, weight='weight')

    # If the dominating set still covers all vertices, it should be the same
    assert original_dom_set == new_dom_set

# End program