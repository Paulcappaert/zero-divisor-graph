import itertools
from zdg.groupoid import Groupoid

'''
gets a simple graph with the given edges
returns a dictionary from vertices to their neighborhoods
'''
def graph_from_edges(*args):
    graph = {}
    for e in args:
        for i in range(2):
            if e[i] in graph:
                graph[e[i]].add(e[1 - i])
            else:
                graph[e[i]] = {e[1 - i]}
    return graph

def _poss_vertex(nhood, graph):
    poss = set()
    for x in graph:
        if (graph[x].union({x})).issuperset(nhood):
            poss.add(x)
    not_empty = len(poss)
    return not_empty, poss

'''
gets the possible products of zero divisors with the given zero element
return a dictionary from products to possible values
if insufficient zdg, returns false and possible products
'''
def poss_mappings(graph, zero=0):
    poss = True
    maps = {}

    for a, b in itertools.combinations(graph, 2):
        if a not in graph[b]:
            nhood = graph[a].union(graph[b])
            not_empty, maps[frozenset({a, b})] = _poss_vertex(nhood, graph)
            poss = not_empty and poss
        else:
            maps[frozenset({a, b})] = {zero}

    for a in graph.keys():
        nhood = graph[a]
        not_empty, maps[frozenset({a})] = _poss_vertex(nhood, graph)
        maps[frozenset({a})].add(zero)
        poss = not_empty and poss
        maps[frozenset({a, zero})] = {zero}

    maps[frozenset({zero})] = {zero}

    return poss, maps

def get_groupoid(graph, zero=0):
    g = Groupoid(graph.keys(), zero=zero)

    for a in graph.keys():
        for b in graph[a]:
            g.set(a, b, zero)

    return g
