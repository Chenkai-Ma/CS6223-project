from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_min_weighted_dominating_set_covers_all_vertices_property():
    G = st.builds(nx.empty_graph, n=st.integers(min_value=0, max_value=100)).example()
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G)
    assert all(v in dom_set or any(adj in dom_set for adj in G[v]) for v in G)

@given(st.data())
def test_min_weighted_dominating_set_subset_of_input_property():
    G = st.builds(nx.empty_graph, n=st.integers(min_value=0, max_value=100)).example()
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G)
    assert dom_set.issubset(G.nodes)

@given(st.data())
def test_min_weighted_dominating_set_minimized_size_property():
    G = st.builds(nx.empty_graph, n=st.integers(min_value=0, max_value=100)).example()
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G)
    for potential_set in st.lists(st.sampled_from(G.nodes), min_size=len(dom_set)-1, max_size=len(G.nodes)).example():
        if all(v in potential_set or any(adj in potential_set for adj in G[v]) for v in G):
            assert len(potential_set) >= len(dom_set)

@given(st.data())
def test_min_weighted_dominating_set_empty_graph_property():
    G = nx.empty_graph(0)
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G)
    assert dom_set == set()

@given(st.data())
def test_min_weighted_dominating_set_non_increasing_cost_effectiveness_property():
    G = st.builds(nx.empty_graph, n=st.integers(min_value=0, max_value=100)).example()
    dom_set = nx.algorithms.approximation.dominating_set.min_weighted_dominating_set(G)
    costs = []
    for node in dom_set:
        neighborhood = {node} | set(G[node])
        cost = G.nodes[node].get('weight', 1) / len(neighborhood - dom_set)
        costs.append(cost)
    assert all(costs[i] >= costs[i+1] for i in range(len(costs) - 1))

# End program