import numpy as np

class ModularCounter():
    '''
    An object for counting every possible unique selection from a
    list of possible elements
    '''
    def __init__(self, mods, elements):
        self.mods = np.array(mods, dtype='uint16')

        if not len(mods) == len(elements):
            raise ValueError('different number of elements and modulos')

        self.element_index = {}
        for i, e in enumerate(elements):
            self.element_index[e] = i

        self.nums = [0] * len(self.mods)
        self.nums = np.zeros((len(self.mods)), dtype='uint16')

    def tick(self):
        carry = 1
        i = 0
        while carry > 0:
            self.nums[i] += 1
            if self.nums[i] % self.mods[i] == 0:
                self.nums[i] = 0
                carry = 1
            else:
                carry = 0
            i += 1
            if i == len(self.mods):
                i = 0
                carry = 0

    def get_count(self, element):
        return self.nums[self.element_index[element]]
