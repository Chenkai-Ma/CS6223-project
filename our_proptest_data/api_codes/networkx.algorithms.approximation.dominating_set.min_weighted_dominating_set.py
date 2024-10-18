@not_implemented_for("directed")
@nx._dispatchable(node_attrs="weight")
def min_weighted_dominating_set(G, weight=None):
    # The unique dominating set for the null graph is the empty set.
    if len(G) == 0:
        return set()

    # This is the dominating set that will eventually be returned.
    dom_set = set()

    def _cost(node_and_neighborhood):
        """Returns the cost-effectiveness of greedily choosing the given
        node.

        `node_and_neighborhood` is a two-tuple comprising a node and its
        closed neighborhood.

        """
        v, neighborhood = node_and_neighborhood
        return G.nodes[v].get(weight, 1) / len(neighborhood - dom_set)

    # This is a set of all vertices not already covered by the
    # dominating set.
    vertices = set(G)
    # This is a dictionary mapping each node to the closed neighborhood
    # of that node.
    neighborhoods = {v: {v} | set(G[v]) for v in G}

    # Continue until all vertices are adjacent to some node in the
    # dominating set.
    while vertices:
        # Find the most cost-effective node to add, along with its
        # closed neighborhood.
        dom_node, min_set = min(neighborhoods.items(), key=_cost)
        # Add the node to the dominating set and reduce the remaining
        # set of nodes to cover.
        dom_set.add(dom_node)
        del neighborhoods[dom_node]
        vertices -= min_set

    return dom_set