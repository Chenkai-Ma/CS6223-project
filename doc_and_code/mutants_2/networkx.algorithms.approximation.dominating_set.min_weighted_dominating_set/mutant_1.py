# property to violate: The output set of nodes is a subset of the input graph's nodes, meaning all nodes in the dominating set must be present in the original graph \( G \).
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import min_weighted_dominating_set

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_dominating_set_min_weighted_dominating_set_1():
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    dominating_set = min_weighted_dominating_set(G)

    # Modify the output to include a node not in the original graph
    dominating_set.add(max(G.nodes) + 1)

    # Check that all nodes in the dominating set are part of the original graph
    assert dominating_set.issubset(G.nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_dominating_set_min_weighted_dominating_set_2():
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    dominating_set = min_weighted_dominating_set(G)

    # Add a node that is not in the original graph
    dominating_set = dominating_set.union({-1})

    # Check that all nodes in the dominating set are part of the original graph
    assert dominating_set.issubset(G.nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_dominating_set_min_weighted_dominating_set_3():
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    dominating_set = min_weighted_dominating_set(G)

    # Introduce a completely arbitrary node
    dominating_set = dominating_set.union({999})

    # Check that all nodes in the dominating set are part of the original graph
    assert dominating_set.issubset(G.nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_dominating_set_min_weighted_dominating_set_4():
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    dominating_set = min_weighted_dominating_set(G)

    # Remove an element and add a non-existent node
    dominating_set.pop()
    dominating_set.add(42)

    # Check that all nodes in the dominating set are part of the original graph
    assert dominating_set.issubset(G.nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_dominating_set_min_weighted_dominating_set_5():
    G = data.draw(st.builds(nx.Graph, edges=st.lists(st.tuples(st.integers(), st.integers()), min_size=1)))
    dominating_set = min_weighted_dominating_set(G)

    # Forcefully add a node that is guaranteed not to be in the graph
    dominating_set = dominating_set.union({len(G.nodes)})

    # Check that all nodes in the dominating set are part of the original graph
    assert dominating_set.issubset(G.nodes)