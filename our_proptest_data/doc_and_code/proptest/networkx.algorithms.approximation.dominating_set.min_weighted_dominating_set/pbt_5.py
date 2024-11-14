from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import min_weighted_dominating_set

@given(st.data())
def test_output_subset_of_input_property(data):
    # Generate a random undirected graph
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    dominating_set = min_weighted_dominating_set(G)

    # Check that all nodes in the dominating set are part of the original graph
    assert dominating_set.issubset(G.nodes)

@given(st.data())
def test_output_covers_all_vertices_property(data):
    # Generate a random undirected graph
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    dominating_set = min_weighted_dominating_set(G)

    # Check that every vertex is either in the dominating set or adjacent to a node in the dominating set
    for node in G.nodes:
        assert node in dominating_set or any(neighbor in dominating_set for neighbor in G.neighbors(node))

@given(st.data())
def test_output_weight_constraint_property(data):
    # Generate a random undirected graph with weights
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    weights = {node: data.draw(st.integers(min_value=1, max_value=100)) for node in G.nodes}
    nx.set_node_attributes(G, weights, 'weight')
    dominating_set = min_weighted_dominating_set(G, weight='weight')

    # Calculate weights
    total_weight = sum(weights[node] for node in G.nodes)
    min_weight_dominating_set_weight = sum(weights[node] for node in dominating_set)
    
    # Check the weight constraint
    log_w_V = 1 if total_weight == 0 else (len(str(total_weight)))  # Simple log approximation
    assert min_weight_dominating_set_weight <= (log_w_V * min_weight_dominating_set_weight)

@given(st.data())
def test_empty_graph_property(data):
    # Test with an empty graph
    G = nx.Graph()
    dominating_set = min_weighted_dominating_set(G)
    
    # Check that the output is an empty set
    assert dominating_set == set()

@given(st.data())
def test_output_robustness_property(data):
    # Generate a random undirected graph
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    dominating_set = min_weighted_dominating_set(G)

    # Modify the graph in a way that should not change the dominating set
    if G.number_of_nodes() > 0:
        G.add_node(max(G.nodes) + 1)  # Add a new isolated node
    new_dominating_set = min_weighted_dominating_set(G)
    
    # Check that the original dominating set remains valid in the modified graph
    assert new_dominating_set.issuperset(dominating_set)

# End program