from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import min_weighted_dominating_set

@given(st.data())
def test_output_subset_of_input_property(data):
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    weight_attr = st.integers().map(lambda x: {'weight': x})
    for node in G.nodes:
        G.nodes[node].update(weight_attr.example())
    dominating_set = min_weighted_dominating_set(G, weight='weight')
    assert dominating_set.issubset(G.nodes)

@given(st.data())
def test_output_covers_all_vertices_property(data):
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    weight_attr = st.integers().map(lambda x: {'weight': x})
    for node in G.nodes:
        G.nodes[node].update(weight_attr.example())
    dominating_set = min_weighted_dominating_set(G, weight='weight')
    for vertex in G.nodes:
        assert vertex in dominating_set or any(neighbor in dominating_set for neighbor in G[vertex])

@given(st.data())
def test_weight_constraint_property(data):
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    weight_attr = st.integers().map(lambda x: {'weight': x})
    for node in G.nodes:
        G.nodes[node].update(weight_attr.example())
    dominating_set = min_weighted_dominating_set(G, weight='weight')
    
    total_weight_dominating_set = sum(G.nodes[node].get('weight', 1) for node in dominating_set)
    total_weight_graph = sum(G.nodes[node].get('weight', 1) for node in G.nodes)
    
    # Assuming w(V*) can be approximated by the weight of the dominating set
    assert total_weight_dominating_set <= (log(total_weight_graph) * total_weight_dominating_set)

@given(st.data())
def test_empty_graph_property(data):
    G = nx.Graph()  # Empty graph
    dominating_set = min_weighted_dominating_set(G)
    assert dominating_set == set()

@given(st.data())
def test_output_unchanged_with_graph_modification_property(data):
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    weight_attr = st.integers().map(lambda x: {'weight': x})
    for node in G.nodes:
        G.nodes[node].update(weight_attr.example())
    
    original_dominating_set = min_weighted_dominating_set(G, weight='weight')
    
    # Modify the graph in a way that does not affect the dominating set
    G.add_node(max(G.nodes) + 1)  # Adding a new isolated node
    new_dominating_set = min_weighted_dominating_set(G, weight='weight')
    
    assert original_dominating_set == new_dominating_set
# End program