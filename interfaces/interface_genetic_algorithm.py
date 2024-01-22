from services.cross import Cross
from services.pairing import Pairing
from services.mutation import Mutation
from services.pruning import Pruning


class IGeneticAlgorithm:
    def __init__(self):
        self.pruning = Pruning
        self.cross = Cross
        self.pairing = Pairing
        self.mutation = Mutation

    def pruning_class(self, population, best, p_max):
        return self.pruning(population, best, p_max)

    def cross_class(self, population, crossover):
        return self.cross(population, crossover)

    def pairing_class(self, p):
        return self.pairing(p)

    def mutation_class(self, children, imp, gmp):
        return self.mutation(children, imp, gmp)
