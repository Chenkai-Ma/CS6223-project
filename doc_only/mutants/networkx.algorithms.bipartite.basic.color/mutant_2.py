# property to violate: Each node in the output dictionary must be assigned a color value of either 0 or 1.
from hypothesis import given, strategies as st
import networkx as nx
from networkx.algorithms import bipartite

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_1():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Modify the output to include a value of 2
        c[0] = 2
        for color in c.values():
            assert color in {0, 1}

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_2():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Modify the output to include a value of -1
        c[1] = -1
        for color in c.values():
            assert color in {0, 1}

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_3():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Modify the output to include a string value
        c[2] = "color"
        for color in c.values():
            assert color in {0, 1}

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_4():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Modify the output to include a float value
        c[3] = 0.5
        for color in c.values():
            assert color in {0, 1}

@given(st.data())
def test_violation_of_networkx_algorithms_bipartite_basic_color_5():
    G = data.draw(st.builds(nx.Graph, nodes=st.lists(st.integers(), min_size=1)))
    if bipartite.is_bipartite(G):
        c = bipartite.color(G)
        # Modify the output to include a None value
        c[4] = None
        for color in c.values():
            assert color in {0, 1}