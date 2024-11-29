from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_subset_of_input_property(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    weight_attr = data.draw(st.one_of(st.none(), st.text()))
    
    if weight_attr is not None:
        for node in G.nodes:
            G.nodes[node][weight_attr] = data.draw(st.integers(min_value=1, max_value=10))
    
    dominating_set = nx.approximation.min_weighted_dominating_set(G, weight=weight_attr)
    
    assert dominating_set.issubset(G.nodes)

@given(st.data())
def test_output_covers_all_vertices_property(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    weight_attr = data.draw(st.one_of(st.none(), st.text()))
    
    if weight_attr is not None:
        for node in G.nodes:
            G.nodes[node][weight_attr] = data.draw(st.integers(min_value=1, max_value=10))
    
    dominating_set = nx.approximation.min_weighted_dominating_set(G, weight=weight_attr)
    
    all_vertices_covered = all(
        v in dominating_set or any(neighbor in dominating_set for neighbor in G[v]) 
        for v in G.nodes
    )
    assert all_vertices_covered

@given(st.data())
def test_output_weight_limit_property(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    weight_attr = data.draw(st.one_of(st.none(), st.text()))
    
    if weight_attr is not None:
        for node in G.nodes:
            G.nodes[node][weight_attr] = data.draw(st.integers(min_value=1, max_value=10))
    
    dominating_set = nx.approximation.min_weighted_dominating_set(G, weight=weight_attr)

    w_V = sum(G.nodes[n].get(weight_attr, 1) for n in G.nodes)
    w_V_star = sum(G.nodes[n].get(weight_attr, 1) for n in dominating_set)
    
    weight_limit = (nx.utils.log(w_V) if w_V > 1 else 0) * w_V_star
    assert sum(G.nodes[n].get(weight_attr, 1) for n in dominating_set) <= weight_limit

@given(st.data())
def test_empty_graph_property(data):
    G = nx.Graph()  # Create an empty graph
    dominating_set = nx.approximation.min_weighted_dominating_set(G)
    
    assert dominating_set == set()  # Output should be an empty set

@given(st.data())
def test_output_robustness_property(data):
    G = data.draw(st.builds(nx.Graph, st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    weight_attr = data.draw(st.one_of(st.none(), st.text()))
    
    if weight_attr is not None:
        for node in G.nodes:
            G.nodes[node][weight_attr] = data.draw(st.integers(min_value=1, max_value=10))
    
    original_dominating_set = nx.approximation.min_weighted_dominating_set(G, weight=weight_attr)

    # Modify the graph by adding a new edge or node
    if G.number_of_edges() > 0:
        new_edge = (data.draw(st.sampled_from(list(G.nodes))), data.draw(st.sampled_from(list(G.nodes))))
        G.add_edge(*new_edge)

    new_dominating_set = nx.approximation.min_weighted_dominating_set(G, weight=weight_attr)
    
    assert new_dominating_set.issubset(G.nodes)  # Should still be a subset of nodes in G
# End program