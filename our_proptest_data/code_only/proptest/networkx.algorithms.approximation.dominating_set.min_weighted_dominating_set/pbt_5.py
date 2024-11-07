from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_covers_all_vertices_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    weight = data.draw(st.one_of(st.none(), st.dictionaries(st.integers(), st.integers(min_value=1))))
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G, weight)
    for node in G.nodes:
        assert node in dom_set or any(neighbor in dom_set for neighbor in G.neighbors(node))

@given(st.data())
def test_output_is_subset_of_input_vertices_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    weight = data.draw(st.one_of(st.none(), st.dictionaries(st.integers(), st.integers(min_value=1))))
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G, weight)
    assert dom_set.issubset(G.nodes)

@given(st.data())
def test_size_of_output_is_minimized_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    weight = data.draw(st.one_of(st.none(), st.dictionaries(st.integers(), st.integers(min_value=1))))
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G, weight)
    for candidate in st.lists(st.integers(), min_size=1).example():
        if all(node in G.nodes for node in candidate):
            candidate_set = set(candidate)
            if all(node in candidate_set or any(neighbor in candidate_set for neighbor in G.neighbors(node)) for node in G.nodes):
                assert len(dom_set) <= len(candidate_set)

@given(st.data())
def test_empty_graph_output_is_empty_set_property(data):
    G = nx.Graph()  # Empty graph
    weight = data.draw(st.one_of(st.none(), st.dictionaries(st.integers(), st.integers(min_value=1))))
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G, weight)
    assert dom_set == set()

@given(st.data())
def test_non_increasing_cost_effectiveness_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    weight = data.draw(st.one_of(st.none(), st.dictionaries(st.integers(), st.integers(min_value=1))))
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G, weight)
    
    # Check cost-effectiveness
    costs = []
    for node in dom_set:
        neighborhood = {node} | set(G.neighbors(node))
        cost_effectiveness = G.nodes[node].get(weight, 1) / len(neighborhood - dom_set)
        costs.append(cost_effectiveness)

    assert all(costs[i] >= costs[i + 1] for i in range(len(costs) - 1))

# End program