import networkx as nx

# Buggy version 1: Removing the last element of each edge tuple
def buggy_1(G, source=None, orientation=None):
    cycle = nx.find_cycle(G, source=source, orientation=orientation)
    return [edge[:-1] for edge in cycle]

# Buggy version 2: Replacing the last element of each edge tuple with a wrong value
def buggy_2(G, source=None, orientation=None):
    cycle = nx.find_cycle(G, source=source, orientation=orientation)
    return [(edge[0], edge[1], 'wrong') for edge in cycle]

# Buggy version 3: Reversing the order of 'forward' and 'reverse' in the edge tuples
def buggy_3(G, source=None, orientation=None):
    cycle = nx.find_cycle(G, source=source, orientation=orientation)
    return [(edge[0], edge[1], 'reverse' if edge[2] == 'forward' else 'forward') for edge in cycle]

# Buggy version 4: Ignoring the orientation argument and always specifying the direction as 'forward'
def buggy_4(G, source=None, orientation=None):
    cycle = nx.find_cycle(G, source=source, orientation=orientation)
    return [(edge[0], edge[1], 'forward') for edge in cycle]

# Buggy version 5: Ignoring the orientation argument and always specifying the direction as 'reverse'
def buggy_5(G, source=None, orientation=None):
    cycle = nx.find_cycle(G, source=source, orientation=orientation)
    return [(edge[0], edge[1], 'reverse') for edge in cycle]