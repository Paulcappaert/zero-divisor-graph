from zdg.graph import graph_from_edges, poss_mappings, get_groupoid
from zdg.semigroup import reduce_poss_maps, get_semigroups, convert_pm
from zdg.groupoid import Groupoid

class ZeroDivisorGraph():

    def __init__(self, *edges):
        self.graph = graph_from_edges(*edges)

    def is_sufficient(self):
        sufficient, _ = poss_mappings(self.graph, zero=0)
        return sufficient

    def poss_maps(self, zero=0):
        sufficient, poss_maps = poss_mappings(self.graph, zero=zero)
        poss_maps = convert_pm(poss_maps, groupoid.elements)
        reduce_poss_maps(poss_maps, len(self.graph) + 1)
        return poss_maps

    def semigroups(self, zero=0):
        sufficient, poss_maps = poss_mappings(self.graph, zero=zero)
        groupoid = Groupoid(self.graph.keys(), zero=zero)
        poss_maps = convert_pm(poss_maps, groupoid.elements)
        if sufficient:
            reduce_poss_maps(poss_maps, groupoid.size)
            return get_semigroups(poss_maps, groupoid)
        else:
            return set()
