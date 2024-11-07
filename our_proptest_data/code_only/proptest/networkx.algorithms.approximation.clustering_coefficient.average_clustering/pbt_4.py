from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms.approximation import average_clustering

@given(st.data())
def test_average_clustering_non_negative_property(data):
    G = data.draw(stGraphs())
    result = average_clustering(G)
    assert result >= 0

@given(st.data())
def test_average_clustering_upper_bound_property(data):
    G = data.draw(stGraphs())
    result = average_clustering(G)
    assert result <= 1

@given(st.data())
def test_average_clustering_empty_graph_property(data):
    G = nx.Graph()  # Creating an empty graph
    result = average_clustering(G)
    assert result == 0

@given(st.data())
def test_average_clustering_consistency_property(data):
    G = data.draw(stGraphs())
    seed = data.draw(st.integers())  # Use a random integer seed
    result1 = average_clustering(G, seed=seed)
    result2 = average_clustering(G, seed=seed)
    assert result1 == result2

@given(st.data())
def test_average_clustering_invariance_property(data):
    G = data.draw(stGraphs())
    result1 = average_clustering(G)
    result2 = average_clustering(nx.relabel_nodes(G, {n: n for n in G.nodes()}))  # Relabeling should not change the result
    assert result1 == result2
# End program
``` 

Note: The testing strategy `stGraphs()` needs to be defined or imported appropriately to generate graphs, which is not shown here. You might want to use `st.graphs()` or a similar strategy depending on your specific implementation context.