# property to violate: The output should be consistent with the maximum degree of any node in the graph; it cannot be larger than the maximum degree plus one, as cliques are formed by connected nodes.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import large_clique_size

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_clique_large_clique_size_1():
    G = data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1).map(nx.Graph))
    result = large_clique_size(G)
    max_degree = max(dict(G.degree()).values())
    result = max_degree + 2  # Violate the property by making result larger than max_degree + 1
    assert result <= max_degree + 1

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_clique_large_clique_size_2():
    G = data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1).map(nx.Graph))
    result = large_clique_size(G)
    max_degree = max(dict(G.degree()).values())
    result = max_degree + 3  # Violate the property by making result larger than max_degree + 1
    assert result <= max_degree + 1

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_clique_large_clique_size_3():
    G = data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1).map(nx.Graph))
    result = large_clique_size(G)
    max_degree = max(dict(G.degree()).values())
    result = max_degree + 10  # Violate the property by making result larger than max_degree + 1
    assert result <= max_degree + 1

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_clique_large_clique_size_4():
    G = data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1).map(nx.Graph))
    result = large_clique_size(G)
    max_degree = max(dict(G.degree()).values())
    result = max_degree + 5  # Violate the property by making result larger than max_degree + 1
    assert result <= max_degree + 1

@given(st.data())
def test_violation_of_networkx_algorithms_approximation_clique_large_clique_size_5():
    G = data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1).map(nx.Graph))
    result = large_clique_size(G)
    max_degree = max(dict(G.degree()).values())
    result = max_degree + 20  # Violate the property by making result larger than max_degree + 1
    assert result <= max_degree + 1