import networkx as nx

# Buggy version 1: Returns only flow value
def buggy_1(flowG, _s, _t, capacity='capacity', flow_func=None, **kwargs):
    flow_value, flow_dict = nx.maximum_flow(flowG, _s, _t, capacity, flow_func, **kwargs)
    return flow_value

# Buggy version 2: Returns only flow dictionary
def buggy_2(flowG, _s, _t, capacity='capacity', flow_func=None, **kwargs):
    flow_value, flow_dict = nx.maximum_flow(flowG, _s, _t, capacity, flow_func, **kwargs)
    return flow_dict

# Buggy version 3: Returns the tuple reversed
def buggy_3(flowG, _s, _t, capacity='capacity', flow_func=None, **kwargs):
    flow_value, flow_dict = nx.maximum_flow(flowG, _s, _t, capacity, flow_func, **kwargs)
    return flow_dict, flow_value 

# Buggy version 4: Adds an unnecessary third output
def buggy_4(flowG, _s, _t, capacity='capacity', flow_func=None, **kwargs):
    flow_value, flow_dict = nx.maximum_flow(flowG, _s, _t, capacity, flow_func, **kwargs)
    return flow_value, flow_dict, "Unnecessary output"

# Buggy version 5: Returns string output instead of maximum flow value
def buggy_5(flowG, _s, _t, capacity='capacity', flow_func=None, **kwargs):
    flow_value, flow_dict = nx.maximum_flow(flowG, _s, _t, capacity, flow_func, **kwargs)
    flow_value = "This is a string"
    return flow_value, flow_dict