import random
import utilities.utility as utility


class Mutation:
    def __init__(self, children, imp, gmp):
        self.children = children
        self.imp = imp
        self.gmp = gmp

    def mutation(self):
        for i in range(len(self.children)):
            if round(random.uniform(0, 1.0001), 4) >= self.imp:
                bits = list(self.children[i].individual_bits)
                for j in range(len(bits)):
                    if round(random.uniform(0, 1.0001), 4) < self.gmp:
                        reverse = '1' if bits[j] == '0' else '0'
                        bits[j] = reverse
                self.children[i].individual_bits = ''.join(bits)
                self.children[i].individual_num = utility.from_bits_to_number(self.children[i].individual_bits)
        return self.children
