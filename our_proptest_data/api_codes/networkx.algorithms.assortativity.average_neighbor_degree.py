@nx._dispatchable(edge_attrs="weight")
def average_neighbor_degree(G, source="out", target="out", nodes=None, weight=None):
    if G.is_directed():
        if source == "in":
            source_degree = G.in_degree
        elif source == "out":
            source_degree = G.out_degree
        elif source == "in+out":
            source_degree = G.degree
        else:
            raise nx.NetworkXError(
                f"source argument {source} must be 'in', 'out' or 'in+out'"
            )

        if target == "in":
            target_degree = G.in_degree
        elif target == "out":
            target_degree = G.out_degree
        elif target == "in+out":
            target_degree = G.degree
        else:
            raise nx.NetworkXError(
                f"target argument {target} must be 'in', 'out' or 'in+out'"
            )
    else:
        if source != "out" or target != "out":
            raise nx.NetworkXError(
                f"source and target arguments are only supported for directed graphs"
            )
        source_degree = target_degree = G.degree

    # precompute target degrees -- should *not* be weighted degree
    t_deg = dict(target_degree())

    # Set up both predecessor and successor neighbor dicts leaving empty if not needed
    G_P = G_S = {n: {} for n in G}
    if G.is_directed():
        # "in" or "in+out" cases: G_P contains predecessors
        if "in" in source:
            G_P = G.pred
        # "out" or "in+out" cases: G_S contains successors
        if "out" in source:
            G_S = G.succ
    else:
        # undirected leave G_P empty but G_S is the adjacency
        G_S = G.adj

    # Main loop: Compute average degree of neighbors
    avg = {}
    for n, deg in source_degree(nodes, weight=weight):
        # handle degree zero average
        if deg == 0:
            avg[n] = 0.0
            continue

        # we sum over both G_P and G_S, but one of the two is usually empty.
        if weight is None:
            avg[n] = (
                sum(t_deg[nbr] for nbr in G_S[n]) + sum(t_deg[nbr] for nbr in G_P[n])
            ) / deg
        else:
            avg[n] = (
                sum(dd.get(weight, 1) * t_deg[nbr] for nbr, dd in G_S[n].items())
                + sum(dd.get(weight, 1) * t_deg[nbr] for nbr, dd in G_P[n].items())
            ) / deg
    return avg