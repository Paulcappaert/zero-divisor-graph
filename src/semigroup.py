
def _inverse_set(a, b, pm, elements):
    '''
    returns: set of values z such that az = b is a possible mapping
    '''
    inv = set()
    for z in elements:
        if b in pm[frozenset({a, z})]:
            inv.add(z)
    return inv

def reduce_poss_maps(poss_maps, elements):
    '''
    parameter: dict of possible mappings for a groupoid
    returns: dict of possible associative mappings
             None if there is no associative mappings
    '''
    for _ in range(len(poss_maps)):
        for a in elements:
            for b in elements:
                for c in elements:
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
                        ab_vals.update(_inverse_set(c, p, poss_maps, elements))

                    bc_vals = set()
                    for p in products:
                        bc_vals.update(_inverse_set(a, p, poss_maps, elements))

                    poss_maps[frozenset({a, b})].intersection_update(ab_vals)
                    poss_maps[frozenset({b, c})].intersection_update(bc_vals)

def _get_semigroup(poss_maps, counter):
    pass

def get_semigroups(poss_maps):
    pass
