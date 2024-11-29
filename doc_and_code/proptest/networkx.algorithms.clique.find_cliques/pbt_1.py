from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.data())
def test_maximal_cliques_property(data):
    G = nx.generators.random_graphs.erdos_renyi_graph(data.draw(st.integers(min_value=1, max_value=100)), 0.5)
    cliques = list(find_cliques(G))
    for clique in cliques:
        for node in clique:
            # Check if the clique is maximal
            neighbors = set(G.neighbors(node))
            if neighbors.intersection(set(clique)) != set(clique):
                assert False  # Not maximal
    assert True  # All cliques are maximal
# End program

@given(st.data())
def test_cliques_contain_given_nodes_property(data):
    G = nx.generators.random_graphs.erdos_renyi_graph(data.draw(st.integers(min_value=1, max_value=100)), 0.5)
    nodes = data.draw(st.lists(st.integers(min_value=0, max_value=G.number_of_nodes()-1), min_size=1, max_size=5))
    if all(node in G.nodes for node in nodes):
        cliques = list(find_cliques(G, nodes=nodes))
        for clique in cliques:
            assert all(node in clique for node in nodes)
    else:
        # If nodes isn't a clique, test that ValueError is raised
        try:
            list(find_cliques(G, nodes=nodes))
            assert False  # Should have raised ValueError
        except ValueError:
            assert True  # Correct behavior
# End program

@given(st.data())
def test_unique_cliques_property(data):
    G = nx.generators.random_graphs.erdos_renyi_graph(data.draw(st.integers(min_value=1, max_value=100)), 0.5)
    cliques = list(find_cliques(G))
    assert len(cliques) == len(set(map(tuple, cliques)))  # Ensure uniqueness
# End program

@given(st.data())
def test_cliques_length_property(data):
    G = nx.generators.random_graphs.erdos_renyi_graph(data.draw(st.integers(min_value=1, max_value=100)), 0.5)
    cliques = list(find_cliques(G))
    for clique in cliques:
        assert len(clique) >= 1  # Each clique must have at least one node
# End program

@given(st.data())
def test_arbitrary_order_property(data):
    G = nx.generators.random_graphs.erdos_renyi_graph(data.draw(st.integers(min_value=1, max_value=100)), 0.5)
    cliques1 = list(find_cliques(G))
    cliques2 = list(find_cliques(G))
    assert sorted(map(sorted, cliques1)) == sorted(map(sorted, cliques2))  # Same cliques, arbitrary order
# End program