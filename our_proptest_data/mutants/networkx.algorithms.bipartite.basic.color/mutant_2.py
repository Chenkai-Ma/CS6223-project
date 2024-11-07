# property to violate: Each node in the output dictionary must be assigned a color value of either 0 or 1.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import bipartite

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_1():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Modify output to always assign color 2
        for node in c.keys():
            c[node] = 2
        for color in c.values():
            assert color in {0, 1}

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_2():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Modify output to always assign color -1
        for node in c.keys():
            c[node] = -1
        for color in c.values():
            assert color in {0, 1}

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_3():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Modify output to always assign color 3
        for node in c.keys():
            c[node] = 3
        for color in c.values():
            assert color in {0, 1}

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_4():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Modify output to always assign color 4
        for node in c.keys():
            c[node] = 4
        for color in c.values():
            assert color in {0, 1}

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_5():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Modify output to always assign color None
        for node in c.keys():
            c[node] = None
        for color in c.values():
            assert color in {0, 1}