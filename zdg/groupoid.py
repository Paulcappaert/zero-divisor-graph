import numpy as np

class Groupoid:

    def __init__(self, elements, comm=True, zero=0):
        self.elements = (zero,) + tuple(elements)
        self.comm = comm
        self.size = len(self.elements)
        self.mult_table = np.zeros((self.size, self.size), dtype='uint16')

    def get(self, a, b):
        return self.mult_table[a][b]

    def set(self, a, b, prod):
        if self.comm:
            self.mult_table[a][b] = prod
            self.mult_table[b][a] = prod
        else:
            self.mult_table[a][b] = prod

    def copy(self):
        g = Groupoid(self.elements[1:], comm=self.comm, zero=self.elements[0])
        g.mult_table = self.mult_table.copy()
        return g

    def caley_table(self):
        ret_val = '*|\t'
        for a in self.elements:
            ret_val += f'{a}|\t'
        ret_val += '\n'
        for a in range(self.size):
            ret_val += str(self.elements[a]) + '|\t'
            for b in range(self.size):
                product = self.elements[self.get(a, b)]
                ret_val += f'{product},\t'
            ret_val += '\n'
        return ret_val


def is_assoc(groupoid):
    for a in range(groupoid.size):
        for b in range(groupoid.size):
            for c in range(groupoid.size):
                p1 = groupoid.get(a, groupoid.get(b, c))
                p2 = groupoid.get(groupoid.get(a, b), c)
                if not p1 == p2:
                    return False
    return True
