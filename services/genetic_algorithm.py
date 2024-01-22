from interfaces.interface_genetic_algorithm import IGeneticAlgorithm
import utilities.utility as utility


def save_statistics(population, optimization):
    fitness = [p.fx for p in population]

    if optimization == "Maximización":
        best = max(fitness)
        worst = min(fitness)
    else:
        best = min(fitness)
        worst = max(fitness)

    average_evaluated = sum(fitness) / len(fitness)

    individual_best = None
    individual_worst = None

    for x in population:
        if x.fx == best:
            individual_best = x
        if x.fx == worst:
            individual_worst = x

    return {"best": individual_best, "worst": individual_worst, "average": average_evaluated}


class GeneticAlgorithm:
    def __init__(self, entries):
        self.initial_population = int(entries["ip"].get())
        self.maximum_population = int(entries["mp"].get())
        # self.crossover_probability = float(entries["cp"].get())
        self.individual_mutation_probability = float(entries["imp"].get())
        self.gen_mutation_probability = float(entries["gmp"].get())
        self.a = float(entries["a"].get())
        self.b = float(entries["b"].get())
        self.desired_result = float(entries["dr"].get())
        self.iterations = int(entries["i"].get())
        # self.n = int(entries["n"].get())
        self.optimization = entries["optimization"].get()
        self.interface_genetic_algorithm = IGeneticAlgorithm()
        self.ranges = utility.ranges(self.a, self.b)
        self.jumps = utility.jumps(self.ranges, self.desired_result)
        self.points = utility.numbers_points(self.jumps)
        self.numbers_bits = utility.numbers_bits(self.points)
        self.delta_x = utility.delta_x_optimal(self.ranges, self.numbers_bits, self.desired_result)
        self.crossover = utility.static_cross(self.numbers_bits)
        self.population_for_generation = []
        self.population_for_generation_before_pruning = []

    # Maybe put Equation of interface (equation, children_mutated, size_population)
    def evaluate_aptitude(self, children_mutated, size_population):
        x_list = [utility.x(self.a, i.individual_num, self.delta_x) for i in children_mutated]
        fx_list = [utility.evaluation_function(x) for x in x_list]
        for x, value in enumerate(children_mutated):
            value.id = size_population + x
            value.fx = fx_list[x]
            value.x = x_list[x]
        return children_mutated

    # Maybe put Equation of interface (equation, generation)
    def generate_population_initial(self, generation):
        numbers_random = []
        while len(numbers_random) < self.initial_population:
            number = utility.generate_random_number(self.numbers_bits)
            if number not in numbers_random:
                numbers_random.append(number)
        bits_random = [utility.from_number_to_bits(x, self.numbers_bits) for x in numbers_random]
        x = [utility.x(self.a, i, self.delta_x) for i in numbers_random]
        # Equation in the (x, equation)
        fx = [utility.evaluation_function(x_fx) for x_fx in x]
        return [utility.create_individual(j, value, bits_random[j], x[j], fx[j], generation) for j, value in
                enumerate(numbers_random)]

    def genetic_algorithm(self):
        list_statistics = []
        population_for_g = {}
        # Maybe put Equation of interface (equation, generation)
        population_initial = self.generate_population_initial(0)
        self.population_for_generation_before_pruning.extend(population_initial)
        if 0 not in population_for_g:
            population_for_g[0] = []
        population_for_g[0].append(population_initial)
        self.population_for_generation.extend(population_initial)
        statistics = save_statistics(population_initial, self.optimization)
        list_statistics.append(statistics)
        population = population_initial
        for x in range(self.iterations):
            # print("Genetation", (x + 1))
            if len(population) > 1:
                # Generate couples
                couples = self.interface_genetic_algorithm.pairing_class(population).couples()
                # Generate crossover
                children = self.interface_genetic_algorithm.cross_class(couples, self.crossover).crossover_pairs(x)
                # Mutating
                children_mutated = self.interface_genetic_algorithm.mutation_class(children,
                                                                                   self.individual_mutation_probability,
                                                                                   self.gen_mutation_probability).mutation()
                # Evaluation aptitude
                children_evaluated = self.evaluate_aptitude(children_mutated, len(population))
                self.population_for_generation_before_pruning = self.population_for_generation_before_pruning + children_evaluated
                # Add to population
                population_v2 = population + children_evaluated
                if (x + 1) not in population_for_g:
                    population_for_g[(x + 1)] = []
                population_for_g[(x + 1)].append(population_v2)
                self.population_for_generation = self.population_for_generation + population_v2
                population = population_v2
                # Save statistics
                statistics = save_statistics(population, self.optimization)
                list_statistics.append(statistics)
                # Do pruning
                population_pruning = self.interface_genetic_algorithm.pruning_class(population, statistics["best"],
                                                                                    self.maximum_population).pruning_function()
                population = population_pruning
        return population, list_statistics, self.population_for_generation, self.population_for_generation_before_pruning, population_for_g
