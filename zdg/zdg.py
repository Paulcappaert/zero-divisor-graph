from zdg.graph import graph_from_edges, poss_mappings, get_groupoid
from zdg.semigroup import reduce_poss_maps, get_semigroups

class ZeroDivisorGraph():

    def __init__(self, *edges):
        self.graph = graph_from_edges(*edges)

    def is_sufficient(self):
        sufficient, _ = poss_mappings(self.graph, zero=0)
        return sufficient

    def poss_maps(self, zero=0):
        sufficient, poss_maps = poss_mappings(self.graph, zero=zero)
        reduce_poss_maps(poss_maps, tuple(self.graph.keys()) + (zero,))
        return poss_maps

    def semigroups(self, zero=0):
        sufficient, poss_maps = poss_mappings(self.graph, zero=zero)
        groupoid = get_groupoid(self.graph, zero=zero)
        if sufficient:
            reduce_poss_maps(poss_maps, tuple(self.graph.keys()) + (zero,))
            return get_semigroups(poss_maps, groupoid)
        else:
            return set()
