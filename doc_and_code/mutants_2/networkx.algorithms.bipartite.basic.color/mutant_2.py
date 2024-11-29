# property to violate: For any two adjacent nodes in the graph, their colors must be different (i.e., if one node is colored 0, its neighbor must be colored 1).
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import bipartite

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_1():
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        for u, v in G.edges:
            c[v] = c[u]  # Force the color of v to be the same as u
            assert c[u] != c[v]

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_2():
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        for u, v in G.edges:
            c[v] = 0  # Force all adjacent nodes to have the same color
            assert c[u] != c[v]

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_3():
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        for u, v in G.edges:
            c[u] = 1  # Force u to have a fixed color
            c[v] = 1  # Force v to have the same color as u
            assert c[u] != c[v]

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_4():
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        for u, v in G.edges:
            c[u] = c[v] = 2  # Set both colors to the same value
            assert c[u] != c[v]

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_5():
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        for u, v in G.edges:
            c[u] = 0  # Assign the same color to both nodes
            c[v] = 0  # Assign the same color to both nodes
            assert c[u] != c[v]