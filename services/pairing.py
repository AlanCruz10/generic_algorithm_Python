import random


class Pairing:
    def __init__(self, population):
        self.population = population
        self.couples_list = []

    def couples(self):
        for individual in self.population:
            n = random.randint(1, len(self.population))
            w = random.randint(0, n)
            couple_individuals = random.sample(self.population, w)
            if individual in couple_individuals:
                couple_individuals.remove(individual)
            for i in couple_individuals:
                self.couples_list.append((individual, i))
        return self.couples_list
