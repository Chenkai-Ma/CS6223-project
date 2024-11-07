from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_covers_all_vertices_property(data):
    G = data.draw(st.builds(nx.graphs.random_graphs.gnm_random_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             m=st.integers(min_value=1, max_value=1000)))
    weight_attr = st.one_of(st.none(), st.dictionaries(st.integers(), st.integers(min_value=1)))
    weight = data.draw(weight_attr)
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G, weight=weight)
    
    for v in G.nodes:
        assert v in dom_set or any(neighbor in dom_set for neighbor in G[v])

@given(st.data())
def test_output_is_subset_of_input_property(data):
    G = data.draw(st.builds(nx.graphs.random_graphs.gnm_random_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             m=st.integers(min_value=1, max_value=1000)))
    weight_attr = st.one_of(st.none(), st.dictionaries(st.integers(), st.integers(min_value=1)))
    weight = data.draw(weight_attr)
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G, weight=weight)
    
    assert dom_set.issubset(G.nodes)

@given(st.data())
def test_output_minimizes_size_property(data):
    G = data.draw(st.builds(nx.graphs.random_graphs.gnm_random_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             m=st.integers(min_value=1, max_value=1000)))
    weight_attr = st.one_of(st.none(), st.dictionaries(st.integers(), st.integers(min_value=1)))
    weight = data.draw(weight_attr)
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G, weight=weight)
    
    # Check that no smaller dominating set exists (this is a simplified check)
    for node in G.nodes:
        smaller_set = dom_set - {node}
        if all(v in smaller_set or any(neighbor in smaller_set for neighbor in G[v]) for v in G.nodes):
            assert False  # Found a smaller dominating set

@given(st.data())
def test_empty_graph_output_property(data):
    G = nx.Graph()  # Empty graph
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G)
    
    assert dom_set == set()

@given(st.data())
def test_cost_effectiveness_non_increasing_property(data):
    G = data.draw(st.builds(nx.graphs.random_graphs.gnm_random_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             m=st.integers(min_value=1, max_value=1000)))
    weight_attr = st.one_of(st.none(), st.dictionaries(st.integers(), st.integers(min_value=1)))
    weight = data.draw(weight_attr)
    
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G, weight=weight)
    
    cost_effectiveness = []
    neighborhoods = {v: {v} | set(G[v]) for v in G}
    
    for node in dom_set:
        neighborhood = neighborhoods[node]
        cost = G.nodes[node].get(weight, 1) / len(neighborhood - dom_set)
        cost_effectiveness.append(cost)
    
    assert all(cost_effectiveness[i] >= cost_effectiveness[i + 1] for i in range(len(cost_effectiveness) - 1))

# End program