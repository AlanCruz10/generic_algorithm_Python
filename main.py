from tkinter import *
from views.window import Window


class Main:
    def __init__(self):
        self.window = Tk()
        self.window_class = Window

    def start_window(self):
        self.window_class(self.window).draw_window()
        self.window.mainloop()

        # self.initial_population = 4
        # self.maximum_population = 15
        # self.probability_cross = 0.75
        # self.probability_mutation_individual = 0.25
        # self.probability_mutation_gen = 0.35
        # self.a = 3
        # self.b = 5
        # self.delta_x = 2 / 31
        # self.iterations = 4


Main().start_window()
