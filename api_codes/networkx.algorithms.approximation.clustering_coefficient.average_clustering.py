@not_implemented_for("directed")
@py_random_state(2)
@nx._dispatchable(name="approximate_average_clustering")
def average_clustering(G, trials=1000, seed=None):
    n = len(G)
    triangles = 0
    nodes = list(G)
    for i in [int(seed.random() * n) for i in range(trials)]:
        nbrs = list(G[nodes[i]])
        if len(nbrs) < 2:
            continue
        u, v = seed.sample(nbrs, 2)
        if u in G[v]:
            triangles += 1
    return triangles / trials