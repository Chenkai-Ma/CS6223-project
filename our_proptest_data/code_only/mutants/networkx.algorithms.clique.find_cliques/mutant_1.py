# property to violate: The output cliques must be subsets of the input graph's nodes, ensuring that all nodes in each returned clique are present in the original graph.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.clique import find_cliques

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_1():
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    cliques.append([max(graph.nodes) + 1])  # Adding a node that is not in the graph
    for clique in cliques:
        assert set(clique).issubset(graph.nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_2():
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    cliques[0] = [node for node in cliques[0]] + [max(graph.nodes) + 2]  # Modifying the first clique to include a non-existent node
    for clique in cliques:
        assert set(clique).issubset(graph.nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_3():
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    cliques = [[node for node in clique] + [max(graph.nodes) + 3] for clique in cliques]  # Adding an invalid node to all cliques
    for clique in cliques:
        assert set(clique).issubset(graph.nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_4():
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    cliques[-1] = [max(graph.nodes) + 4]  # Changing the last clique to be a single invalid node
    for clique in cliques:
        assert set(clique).issubset(graph.nodes)

@given(st.data())
def test_violation_of_networkx_algorithms_clique_find_cliques_5():
    graph = data.draw(st.builds(nx.Graph, nodes=st.sets(st.integers(), min_size=1, max_size=100)))
    cliques = list(find_cliques(graph))
    cliques.append([max(graph.nodes) + 5, max(graph.nodes) + 6])  # Adding a clique with two non-existent nodes
    for clique in cliques:
        assert set(clique).issubset(graph.nodes)