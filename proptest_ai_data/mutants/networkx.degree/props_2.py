import networkx as nx

# Buggy function 1: returns the number of nodes in the graph plus one.
def buggy_1(G, nbunch=None, weight=None):
    degree_dict = nx.degree(G, nbunch, weight)
    degree_dict[len(degree_dict)] = 0
    return degree_dict

# Buggy function 2: returns the number of nodes in the graph minus one.
def buggy_2(G, nbunch=None, weight=None):
    degree_dict = nx.degree(G, nbunch, weight)
    degree_dict.popitem()
    return degree_dict

# Buggy function 3: returns an empty dictionary, regardless of the input.
def buggy_3(G, nbunch=None, weight=None):
    return {}

# Buggy function 4: Doubles the degree count for the first node in the output dictionary
def buggy_4(G, nbunch=None, weight=None):
    degree_dict = nx.degree(G, nbunch, weight)
    first_key = list(degree_dict.keys())[0]
    degree_dict[first_key] *= 2
    return degree_dict

# Buggy function 5: decreases the degree of each node in the graph by 1
def buggy_5(G, nbunch=None, weight=None):
    degree_dict = nx.degree(G, nbunch, weight)
    for key in degree_dict.keys():
        degree_dict[key] -= 1
    return degree_dict