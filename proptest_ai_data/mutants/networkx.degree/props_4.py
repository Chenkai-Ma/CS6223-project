import networkx as nx

# Buggy version 1: Always returns a dictionary, regardless of input.
def buggy_1(G, nbunch=None, weight=None):
    degree = nx.degree(G, nbunch, weight)
    if isinstance(degree, int):
        return {nbunch: degree}
    return degree

# Buggy version 2: Always returns an empty dictionary.
def buggy_2(G, nbunch=None, weight=None):
    return {}

# Buggy version 3: Returns the negation of the degree when a single node is sent as the argument.
def buggy_3(G, nbunch=None, weight=None):
    degree = nx.degree(G, nbunch, weight)
    if isinstance(degree, int):
        return -degree
    return degree

# Buggy version 4: Returns a float when a single node degree is sent as an argument
def buggy_4(G, nbunch=None, weight=None):
    degree = nx.degree(G, nbunch, weight)
    if isinstance(degree, int):
        return float(degree)
    return degree

# Buggy version 5: Returns a string when a single node degree is sent as an argument
def buggy_5(G, nbunch=None, weight=None):
    degree = nx.degree(G, nbunch, weight)
    if isinstance(degree, int):
        return str(degree)
    return degree  