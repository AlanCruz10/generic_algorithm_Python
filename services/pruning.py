import random
import math


def counter_individuals(population):
    individual_counter = 0
    for x, v in population.items():
        individual_counter = individual_counter + len(population[x])
    return individual_counter


def pruning(population_for_classes):
    for key, value in population_for_classes.items():
        if len(population_for_classes[key]) >= 1:
            if len(population_for_classes[key]) == 1:
                i_random = 0
            else:
                i_random = random.randint(0, len(population_for_classes[key]) - 1)
            for x, v in enumerate(population_for_classes[key]):
                if x == i_random:
                    population_for_classes[key].remove(v)
    return population_for_classes


class Pruning:
    def __init__(self, population, best, population_max):
        self.p_max = population_max
        self.best = best
        self.population = population

    def class_width(self, number_classes):
        population_fx = [p.fx for p in self.population]
        type_column = "int64"
        for value in population_fx:
            if value is float:
                type_column = "float64"
                break
        range_limit = max(population_fx) - min(population_fx)
        if type_column == "int64":
            width_class = range_limit / number_classes
            return round(width_class)
        else:
            width_class = range_limit / number_classes
            return width_class

    def limits(self, number_classes, class_width):
        limits_lower = [float(min([p.fx for p in self.population]))]
        for i in range(1, number_classes):
            limits = limits_lower[i - 1] + class_width
            limits_lower.append(limits)
        limits_upper = [limit + class_width for limit in limits_lower]
        return limits_lower, limits_upper

    def create_classes(self):
        number_classes = round(1 + (3.3 * math.log10(int(len(self.population)))))
        class_width = self.class_width(number_classes)
        limits_lower, limits_upper = self.limits(number_classes, class_width)
        pob = self.population
        population_for_classes = {}
        for p in pob:
            if limits_lower[0] <= p.fx <= limits_upper[0]:
                if 0 not in population_for_classes:
                    population_for_classes[0] = []
                population_for_classes[0].append(p)
        for p in pob:
            for j in range(1, number_classes):
                if limits_lower[j] < p.fx <= limits_upper[j]:
                    if j not in population_for_classes:
                        population_for_classes[j] = []
                    population_for_classes[j].append(p)
        last_class = (number_classes - 1)
        for p in pob:
            if p.fx > limits_upper[last_class]:
                if last_class not in population_for_classes:
                    population_for_classes[last_class] = []
                population_for_classes[last_class].append(p)
        return population_for_classes

    def remove_repeats(self):
        unique_individuals = set()
        purging_repeats = []
        for individual in self.population:
            key = (individual.individual_bits, individual.individual_num)
            if key not in unique_individuals:
                unique_individuals.add(key)
                purging_repeats.append(individual)
        return purging_repeats

    def keep_the_best(self, population_without_repeats):
        return [p for p in population_without_repeats if p.fx != self.best.fx]

    def add_best_to_population_purged(self, population):
        population_purged_completed = []
        for k, p in population.items():
            for i in population[k]:
                population_purged_completed.append(i)
        population_purged_completed.append(self.best)
        return population_purged_completed

    def pruning_function(self):
        population_without_repeats = self.remove_repeats()
        population_without_best = self.keep_the_best(population_without_repeats)
        self.population = population_without_best
        population_for_classes = self.create_classes()
        individual_counter = counter_individuals(population_for_classes)
        # pob = pruning(population_for_classes) si se debe de podar si o si descomentar esta linea
        # individual_counter = counter_individuals(pob) esta tambien
        # population_for_classes = pob y esta tambien
        while individual_counter >= self.p_max:
            pob = pruning(population_for_classes)
            individual_counter = counter_individuals(pob)
            population_for_classes = pob
        purged = self.add_best_to_population_purged(population_for_classes)
        return purged
