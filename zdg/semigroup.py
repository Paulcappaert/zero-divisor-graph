from zdg.counter import ModularCounter
from zdg.groupoid import is_assoc

def _inverse_set(a, b, pm, size):
    '''
    returns: set of values z such that az = b is a possible mapping
    '''
    inv = set()
    for z in range(size):
        if b in pm[frozenset({a, z})]:
            inv.add(z)
    return inv

def convert_pm(pm, elements):
    pmi = {}

    for prod, maps in pm.items():

        if len(prod) == 2:
            a, b = prod
            a = elements.index(a)
            b = elements.index(b)
        else:
            a, = prod
            a = elements.index(a)
            b = a

        pmi[frozenset({a, b})] = set()
        for m in maps:
            pmi[frozenset({a, b})].add(elements.index(m))

    return pmi

def reduce_poss_maps(poss_maps, size):
    '''
    parameter: dict of possible mappings for a groupoid
    returns: dict of possible associative mappings
             None if there is no associative mappings
    '''
    for _ in range(len(poss_maps)):
        for a in range(size):
            for b in range(size):
                for c in range(size):
                    ab = poss_maps[frozenset({a, b})]
                    bc = poss_maps[frozenset({b, c})]
                    prod1 = set()
                    for p in ab:
                        prod1.update(poss_maps[frozenset({p, c})])
                    prod2 = set()
                    for p in bc:
                        prod2.update(poss_maps[frozenset({p, a})])
                    products = prod1.intersection(prod2)

                    ab_vals = set()
                    for p in products:
                        ab_vals.update(_inverse_set(c, p, poss_maps, size))

                    bc_vals = set()
                    for p in products:
                        bc_vals.update(_inverse_set(a, p, poss_maps, size))

                    poss_maps[frozenset({a, b})].intersection_update(ab_vals)
                    poss_maps[frozenset({b, c})].intersection_update(bc_vals)

def get_semigroups(poss_maps, groupoid):
    '''
    parameters:
        groupoid with an incomplete mappings
        dictionary of elements of the groupoid to sets of possible mappings for those elements
    returns: a list of groupoids copied from the passed groupoid and completed with
        mappings from the poss_maps parameter
    '''

    num_possibilites = 1
    mods = []
    ordered_mappings = {}
    ordered_keys = tuple(poss_maps.keys())

    for key in ordered_keys:
        ordered_mappings[key] = tuple(poss_maps[key])
        n = len(poss_maps[key])
        mods.append(n)
        num_possibilites *= n

    counter = ModularCounter(mods, ordered_keys)

    semigroups = set()
    for i in range(num_possibilites):

        for key in ordered_mappings:
            c = ordered_mappings[key][counter.get_count(key)]
            if len(key) == 2:
                a, b = key
                groupoid.set(a, b, c)
            else:
                a, = key
                groupoid.set(a, a, c)
        if is_assoc(groupoid):
            semigroups.add(groupoid.copy())

        counter.tick()

    return semigroups
