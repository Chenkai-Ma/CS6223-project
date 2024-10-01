import networkx as nx

def buggy_1(G, source=None, orientation=None):
    try:
        return nx.find_cycle(G, source=source, orientation=orientation)
    except nx.exception.NetworkXNoCycle:
        return None

def buggy_2(G, source=None, orientation=None):
    try:
        cycle = nx.find_cycle(G, source=source, orientation=orientation)
        return cycle
    except nx.exception.NetworkXNoCycle:
        return []

def buggy_3(G, source=None, orientation=None):
    try:
        cycle = nx.find_cycle(G, source=source, orientation=orientation)
        return cycle
    except nx.exception.NetworkXNoCycle:
        return "No cycle found"

def buggy_4(G, source=None, orientation=None):
    try:
        cycle = nx.find_cycle(G, source=source, orientation=orientation)
        return cycle
    except nx.exception.NetworkXNoCycle:
        return [(0, 0)]

def buggy_5(G, source=None, orientation=None):
    try:
        cycle = nx.find_cycle(G, source=source, orientation=orientation)
        return cycle
    except nx.exception.NetworkXNoCycle:
        return [("No", "cycle")]