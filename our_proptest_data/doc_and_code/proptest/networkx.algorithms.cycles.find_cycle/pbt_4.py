from hypothesis import given, strategies as st
import networkx as nx
from networkx.exception import NetworkXNoCycle

@given(st.data())
def test_cycle_found_property(data):
    # Generate a random directed graph
    G = nx.generators.random_graphs.erdos_renyi_graph(n=data.draw(st.integers(min_value=1, max_value=20)), 
                                                       p=0.3, directed=True)
    try:
        cycle = nx.find_cycle(G)
        assert len(cycle) > 0  # Ensure at least one edge in the cycle
    except NetworkXNoCycle:
        pass  # No cycle found is acceptable

@given(st.data())
def test_cycle_closed_loop_property(data):
    # Generate a directed graph with a cycle
    G = nx.DiGraph()
    G.add_edges_from(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=10)))
    
    # Manually ensure there's a cycle
    if len(G.nodes) > 1:
        G.add_edge(list(G.nodes)[0], list(G.nodes)[0])  # Create a self-loop

    try:
        cycle = nx.find_cycle(G)
        # Extract the first and last edges
        tail_first, head_first = cycle[0]
        tail_last, head_last = cycle[-1]
        assert head_last == tail_first  # Ensure the last edge connects to the first edge
    except NetworkXNoCycle:
        pass  # No cycle found is acceptable

@given(st.data())
def test_orientation_respect_property(data):
    # Generate a directed graph
    G = nx.DiGraph()
    edges = data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=10))
    G.add_edges_from(edges)

    try:
        cycle_original = nx.find_cycle(G, orientation="original")
        cycle_reverse = nx.find_cycle(G, orientation="reverse")
        cycle_ignore = nx.find_cycle(G, orientation="ignore")
        
        # Check the orientations
        assert all((u, v) in cycle_original for (u, v) in edges)  # Original orientation
        assert all((v, u) in cycle_reverse for (u, v) in edges)  # Reverse orientation
    except NetworkXNoCycle:
        pass  # No cycle found is acceptable

@given(st.data())
def test_no_cycle_exception_property(data):
    # Generate a Directed Acyclic Graph (DAG)
    G = nx.DiGraph()
    G.add_edges_from(data.draw(st.lists(st.tuples(st.integers(), st.integers()), min_size=1, max_size=10)))
    
    try:
        nx.find_cycle(G)  # Should raise exception if no cycles
    except NetworkXNoCycle:
        assert True  # Exception raised as expected
    else:
        assert False  # If no exception, this is a failure

@given(st.data())
def test_edges_order_in_traversal_property(data):
    # Generate a random directed graph
    G = nx.generators.random_graphs.erdos_renyi_graph(n=data.draw(st.integers(min_value=1, max_value=20)), 
                                                       p=0.3, directed=True)
    try:
        cycle = nx.find_cycle(G)
        # Check if the edges in the cycle are in the order of traversal
        for i in range(len(cycle) - 1):
            assert cycle[i][1] == cycle[i + 1][0]  # Ensure the head of one edge is the tail of the next
    except NetworkXNoCycle:
        pass  # No cycle found is acceptable
# End program