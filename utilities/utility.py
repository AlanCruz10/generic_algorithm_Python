import math
import random
from models.individual import Individual
import numpy as np


def numbers_bits(points):
    return math.ceil(math.log(points, 2))


def numbers_points(jumps_j):
    return jumps_j + 1


def jumps(ranges_r, dx):
    return ranges_r / dx


def ranges(a, b):
    range_real = b - a
    return abs(range_real)


def generate_random_number(number_bits):
    return random.randint(0, (pow(2, number_bits) - 1))


def from_number_to_bits(number, num_bits):
    return format(number, f'0{num_bits}b')


def from_bits_to_number(bits):
    return int(bits, 2)


def delta_x_optimal(ranges_r, number_bits, dr):
    dx = delta_x(ranges_r, number_bits)
    if dr > dx:
        return dx
    else:
        return dr


def delta_x(ranges_r, number_bits):
    return ranges_r / (pow(2, number_bits) - 1)


def x(a, i, dx):
    return a + (i * dx)


# Maybe can be here the equation (equation, x)
def evaluation_function(x_x):
    # pow(x, 3) - 2 * pow(x, 2) * (math.cos(math.radians(x))) + 3
    return (x_x ** 3) - 2 * (x_x ** 2) * (np.cos(x_x)) + 3
    # return x_x ** 3 - (x_x ** 3) * np.cos(x_x * 5.0)


def create_individual(i, value, value_bits, x_x, fx, generation):
    individual_data = {
        "id": i,
        "individual_bits": value_bits,
        "individual_num": value,
        "x": x_x,
        "fx": fx,
        "generation": generation
    }
    return Individual(**individual_data)


def static_cross(number_bits):
    if number_bits % 2 == 0:
        return int(number_bits / 2)
    else:
        return int(math.ceil(number_bits / 2))
