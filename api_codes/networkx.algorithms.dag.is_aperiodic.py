@nx._dispatchable
def is_aperiodic(G):
    if not G.is_directed():
        raise nx.NetworkXError("is_aperiodic not defined for undirected graphs")
    if len(G) == 0:
        raise nx.NetworkXPointlessConcept("Graph has no nodes.")
    s = arbitrary_element(G)
    levels = {s: 0}
    this_level = [s]
    g = 0
    lev = 1
    while this_level:
        next_level = []
        for u in this_level:
            for v in G[u]:
                if v in levels:  # Non-Tree Edge
                    g = gcd(g, levels[u] - levels[v] + 1)
                else:  # Tree Edge
                    next_level.append(v)
                    levels[v] = lev
        this_level = next_level
        lev += 1
    if len(levels) == len(G):  # All nodes in tree
        return g == 1
    else:
        return g == 1 and nx.is_aperiodic(G.subgraph(set(G) - set(levels)))