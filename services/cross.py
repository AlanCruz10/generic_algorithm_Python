import utilities.utility as utility


class Cross:
    def __init__(self, couples, crossover):
        self.couples = couples
        self.crossover = crossover

    def crossover_pairs(self, x):
        children = []
        for pair in self.couples:
            father_one, father_two = pair
            father_one_bits = father_one.individual_bits
            father_two_bits = father_two.individual_bits

            father_one_first_court = father_one_bits[:self.crossover]
            father_one_second_court = father_one_bits[self.crossover:]

            father_two_first_court = father_two_bits[:self.crossover]
            father_two_second_court = father_two_bits[self.crossover:]

            first_son = father_one_first_court + father_two_second_court
            second_son = father_two_first_court + father_one_second_court

            value_one = utility.from_bits_to_number(first_son)
            value_two = utility.from_bits_to_number(second_son)

            children.append(utility.create_individual(1, value_one, first_son, 0, 0, (x + 1)))
            children.append(utility.create_individual(2, value_two, second_son, 0, 0, (x + 1)))

        return children
