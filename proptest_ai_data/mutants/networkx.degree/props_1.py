import networkx as nx

# Buggy version 1 - rounds to nearest decimal
def buggy_1(G, nbunch=None, weight=None):
    degrees = nx.degree(G, nbunch, weight)
    return {node: round(degree + 0.5, 1) for node, degree in degrees}

# Buggy version 2 - increases degree by 1
def buggy_2(G, nbunch=None, weight=None):
    degrees = nx.degree(G, nbunch, weight)
    return {node: degree + 1 for node, degree in degrees}

# Buggy version 3 - decreases degree by 1
def buggy_3(G, nbunch=None, weight=None):
    degrees = nx.degree(G, nbunch, weight)
    return {node: degree - 1 for node, degree in degrees}

# Buggy version 4 - makes degrees float value
def buggy_4(G, nbunch=None, weight=None):
    degrees = nx.degree(G, nbunch, weight)
    return {node: float(degree) for node, degree in degrees}

# Buggy version 5 - multiplies degree by 2
def buggy_5(G, nbunch=None, weight=None):
    degrees = nx.degree(G, nbunch, weight)
    return {node: degree * 2 for node, degree in degrees}