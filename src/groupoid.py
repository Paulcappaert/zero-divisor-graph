from itertools import product

class Groupoid:

    def __init__(self, elements, comm=True, zero=0):
        self.elements = tuple(elements) + (zero,)
        self.comm = comm

        if self.comm:
            self.mult_table = {frozenset({a, b}): zero for (a, b) in product(self.elements, self.elements)}
        else:
            self.mult_table = {(a, b): zero for (a, b) in product(self.elements, self.elements)}

    def get(self, a, b):
        if self.comm:
            return self.mult_table[frozenset({a, b})]
        else:
            return self.mult_table[(a, b)]

    def set(self, a, b, prod):
        if self.comm:
            self.mult_table[frozenset({a, b})] = prod
        else:
            self.mult_table[(a, b)] = prod

    def copy(self):
        g = Groupoid((), self.comm)
        g.elements = self.elements
        g.mult_table = self.mult_table.copy()
        return g


def is_assoc(groupoid):
    for a in groupoid.elements:
        for b in groupoid.elements:
            for c in groupoid.elements:
                p1 = groupoid.get(a, groupoid.get(b, c))
                p2 = groupoid.get(groupoid.get(a, b), c)
                if not p1 == p2:
                    return False
    return True
