from hypothesis import given, strategies as st
import networkx as nx

@given(st.data())
def test_output_cycle_forms_closed_loop_property(data):
    G = data.draw(st.builds(nx.Graph))  # Generate a graph
    source = data.draw(st.one_of([None, st.sampled_from(G.nodes())]))  # Generate a source node
    cycle = nx.algorithms.cycles.find_cycle(G, source)
    
    if cycle:
        first_edge = cycle[0]
        last_edge = cycle[-1]
        tail_first, head_first = first_edge
        tail_last, head_last = last_edge
        assert head_last == tail_first  # Check if the last node connects back to the first node

@given(st.data())
def test_empty_list_for_acyclic_graph_property(data):
    G = data.draw(st.builds(nx.Graph))  # Generate a graph
    if nx.is_directed_acyclic_graph(G):
        cycle = nx.algorithms.cycles.find_cycle(G)
        assert cycle == []  # Check that the output is an empty list

@given(st.data())
def test_cycle_length_greater_than_or_equal_to_three_property(data):
    G = data.draw(st.builds(nx.Graph))  # Generate a graph
    source = data.draw(st.one_of([None, st.sampled_from(G.nodes())]))  # Generate a source node
    cycle = nx.algorithms.cycles.find_cycle(G, source)
    
    if cycle and len(cycle) < 3:
        assert False, "Cycle found with length less than 3."

@given(st.data())
def test_output_cycle_edges_exist_in_input_graph_property(data):
    G = data.draw(st.builds(nx.Graph))  # Generate a graph
    source = data.draw(st.one_of([None, st.sampled_from(G.nodes())]))  # Generate a source node
    cycle = nx.algorithms.cycles.find_cycle(G, source)
    
    for edge in cycle:
        assert edge in G.edges()  # Check that each edge in the cycle exists in the graph

@given(st.data())
def test_reverse_orientation_cycle_property(data):
    G = data.draw(st.builds(nx.DiGraph))  # Generate a directed graph
    source = data.draw(st.sampled_from(G.nodes()))  # Generate a source node
    cycle = nx.algorithms.cycles.find_cycle(G, source, orientation="reverse")
    
    if cycle:
        for edge in cycle:
            tail, head = edge
            assert (head, tail) in G.edges()  # Check that the reversed edge is in the graph
# End program