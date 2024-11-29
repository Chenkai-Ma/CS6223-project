from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import min_weighted_dominating_set

@given(st.lists(st.tuples(st.integers(), st.integers(), st.integers()), min_size=1).map(lambda edges: nx.Graph(edges)))
def test_output_covers_all_vertices_property(G):
    dom_set = min_weighted_dominating_set(G)
    assert all(v in dom_set or any(neighbor in dom_set for neighbor in G[v]) for v in G)

@given(st.lists(st.tuples(st.integers(), st.integers(), st.integers()), min_size=1).map(lambda edges: nx.Graph(edges)))
def test_output_subset_of_input_vertices_property(G):
    dom_set = min_weighted_dominating_set(G)
    assert dom_set.issubset(G.nodes)

@given(st.lists(st.tuples(st.integers(), st.integers(), st.integers()), min_size=1).map(lambda edges: nx.Graph(edges)))
def test_minimized_size_of_output_dominating_set_property(G):
    dom_set = min_weighted_dominating_set(G)
    for size in range(1, len(G.nodes) + 1):
        smaller_set = set(list(G.nodes)[:size])
        if all(v in smaller_set or any(neighbor in smaller_set for neighbor in G[v]) for v in G):
            assert len(smaller_set) >= len(dom_set)

@given(st.lists(st.tuples(st.integers(), st.integers(), st.integers()), min_size=1).map(lambda edges: nx.Graph(edges)))
def test_empty_graph_output_property():
    G = nx.Graph()
    dom_set = min_weighted_dominating_set(G)
    assert dom_set == set()

@given(st.lists(st.tuples(st.integers(), st.integers(), st.integers()), min_size=1).map(lambda edges: nx.Graph(edges)))
def test_non_increasing_cost_effectiveness_property(G):
    dom_set = min_weighted_dominating_set(G)
    neighborhoods = {v: {v} | set(G[v]) for v in G}
    
    costs = []
    for node in dom_set:
        neighborhood = neighborhoods[node]
        cost = G.nodes[node].get('weight', 1) / len(neighborhood - dom_set)
        costs.append(cost)
    
    assert all(costs[i] >= costs[i + 1] for i in range(len(costs) - 1))

# End program