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
        # Modify the coloring to make adjacent nodes the same color
        for u, v in G.edges:
            c[v] = c[u]  # Force v to have the same color as u
        for u, v in G.edges:
            assert c[u] != c[v]

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_2():
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        # Set all node colors to 0
        for node in G.nodes:
            c[node] = 0
        for u, v in G.edges:
            assert c[u] != c[v]

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_3():
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        # Set all node colors to 1
        for node in G.nodes:
            c[node] = 1
        for u, v in G.edges:
            assert c[u] != c[v]

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_4():
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        # Assign the same color to all nodes in the graph
        color_value = 0 if len(G.nodes) % 2 == 0 else 1
        for node in G.nodes:
            c[node] = color_value
        for u, v in G.edges:
            assert c[u] != c[v]

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_5():
    G = data.draw(st.builds(nx.random_graphs.erdos_renyi_graph, 
                             n=st.integers(min_value=1, max_value=100), 
                             p=st.floats(min_value=0, max_value=1)))
    if nx.is_bipartite(G):
        c = bipartite.color(G)
        # Randomly set all colors to either 0 or 1 without regard to adjacency
        import random
        for node in G.nodes:
            c[node] = random.choice([0, 1])
        for u, v in G.edges:
            assert c[u] != c[v]