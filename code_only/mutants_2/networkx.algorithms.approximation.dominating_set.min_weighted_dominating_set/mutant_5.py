# property to violate: The cost-effectiveness of nodes added to the dominating set should be non-increasing; that is, each subsequent node added should have a cost-effectiveness that is less than or equal to that of the previously added node, ensuring a greedy approach is maintained throughout the process.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import min_weighted_dominating_set

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_dominating_set_min_weighted_dominating_set_1():
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
        costs.append(cost + 1)  # Violate by always increasing cost

    assert all(costs[i] >= costs[i + 1] for i in range(len(costs) - 1))

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_dominating_set_min_weighted_dominating_set_2():
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
        costs.append(cost * 2)  # Violate by multiplying cost

    assert all(costs[i] >= costs[i + 1] for i in range(len(costs) - 1))

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_dominating_set_min_weighted_dominating_set_3():
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
        costs.append(cost + 10)  # Violate by adding a constant

    assert all(costs[i] >= costs[i + 1] for i in range(len(costs) - 1))

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_dominating_set_min_weighted_dominating_set_4():
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
        costs.append(cost * 0.5)  # Violate by reducing cost

    assert all(costs[i] >= costs[i + 1] for i in range(len(costs) - 1))

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_dominating_set_min_weighted_dominating_set_5():
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
        costs.append(cost if costs[-1] < cost else costs[-1] + 1)  # Violate by forcing an increase

    assert all(costs[i] >= costs[i + 1] for i in range(len(costs) - 1))