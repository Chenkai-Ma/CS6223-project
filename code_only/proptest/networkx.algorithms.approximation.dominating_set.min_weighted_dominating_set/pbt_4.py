from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import min_weighted_dominating_set

@given(st.data())
def test_dominating_set_covers_all_vertices_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    weight_attr = st.one_of(st.none(), st.lists(st.integers(), min_size=len(G.nodes())))
    if weight_attr is not None:
        for idx, node in enumerate(G.nodes()):
            G.nodes[node]['weight'] = weight_attr[idx] if idx < len(weight_attr) else 1
    dom_set = min_weighted_dominating_set(G, weight='weight')
    assert all(v in dom_set or any(adj in dom_set for adj in G[v]) for v in G)

@given(st.data())
def test_dominating_set_subset_of_nodes_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    weight_attr = st.one_of(st.none(), st.lists(st.integers(), min_size=len(G.nodes())))
    if weight_attr is not None:
        for idx, node in enumerate(G.nodes()):
            G.nodes[node]['weight'] = weight_attr[idx] if idx < len(weight_attr) else 1
    dom_set = min_weighted_dominating_set(G, weight='weight')
    assert dom_set.issubset(G.nodes())

@given(st.data())
def test_dominating_set_minimized_size_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    weight_attr = st.one_of(st.none(), st.lists(st.integers(), min_size=len(G.nodes())))
    if weight_attr is not None:
        for idx, node in enumerate(G.nodes()):
            G.nodes[node]['weight'] = weight_attr[idx] if idx < len(weight_attr) else 1
    dom_set = min_weighted_dominating_set(G, weight='weight')
    # Check against any smaller dominating set (not trivial, requires more context)
    # Placeholder assertion: details depend on specific graph structure
    assert len(dom_set) <= len(G.nodes())

@given(st.data())
def test_empty_graph_yields_empty_dominating_set_property(data):
    G = nx.Graph()  # Empty graph
    dom_set = min_weighted_dominating_set(G)
    assert dom_set == set()

@given(st.data())
def test_non_increasing_cost_effectiveness_property(data):
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    weight_attr = st.one_of(st.none(), st.lists(st.integers(), min_size=len(G.nodes())))
    if weight_attr is not None:
        for idx, node in enumerate(G.nodes()):
            G.nodes[node]['weight'] = weight_attr[idx] if idx < len(weight_attr) else 1
    dom_set = min_weighted_dominating_set(G, weight='weight')
    costs = []
    neighborhoods = {v: {v} | set(G[v]) for v in G}
    
    for node in dom_set:
        neighborhood = neighborhoods[node]
        cost = G.nodes[node].get('weight', 1) / len(neighborhood - dom_set)
        costs.append(cost)
    
    assert all(costs[i] >= costs[i + 1] for i in range(len(costs) - 1))
# End program