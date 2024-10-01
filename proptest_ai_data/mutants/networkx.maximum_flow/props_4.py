import networkx as nx

def buggy_1(G, s, t, capacity='capacity', flow_func=None, **kwargs):
    flow_value, flow_dict = nx.maximum_flow(G, s, t, capacity, flow_func, **kwargs)
    # Adding extra flow to each edge in dictionary, violating property
    for u in flow_dict:
        for v in flow_dict[u]:
            flow_dict[u][v] += 1
    return flow_value, flow_dict

def buggy_2(G, s, t, capacity='capacity', flow_func=None, **kwargs):
    flow_value, flow_dict = nx.maximum_flow(G, s, t, capacity, flow_func, **kwargs)
    # Multiplying each flow in dictionary by capacity, violating property
    for u in flow_dict:
        for v in flow_dict[u]:
            flow_dict[u][v] *= G[u][v][capacity]
    return flow_value, flow_dict

def buggy_3(G, s, t, capacity='capacity', flow_func=None, **kwargs):
    flow_value, flow_dict = nx.maximum_flow(G, s, t, capacity, flow_func, **kwargs)
    # Setting flow of each edge in dictionary to max integer, violating property
    for u in flow_dict:
        for v in flow_dict[u]:
            flow_dict[u][v] = float('inf')
    return flow_value, flow_dict

def buggy_4(G, s, t, capacity='capacity', flow_func=None, **kwargs):
    flow_value, flow_dict = nx.maximum_flow(G, s, t, capacity, flow_func, **kwargs)
    # Setting all flows to negative values, violating property
    for u in flow_dict:
        for v in flow_dict[u]:
            flow_dict[u][v] = -flow_dict[u][v]
    return flow_value, flow_dict

def buggy_5(G, s, t, capacity='capacity', flow_func=None, **kwargs):
    flow_value, flow_dict = nx.maximum_flow(G, s, t, capacity, flow_func, **kwargs)
    # Setting flow of each edge in dictionary to the sum of all capacities, violating property
    total_capacity = sum([attr[capacity] for u, v, attr in G.edges(data=True)])
    for u in flow_dict:
        for v in flow_dict[u]:
            flow_dict[u][v] = total_capacity
    return flow_value, flow_dict