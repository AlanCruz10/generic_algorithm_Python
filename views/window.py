from tkinter import *
from tkinter import ttk
from services.genetic_algorithm import GeneticAlgorithm
from views.graphic_view import Graphic
from views.results_view import Result


def section_ranges(second_menu_panel):
    title_ranges = Label(second_menu_panel, text='Ranges', bg='#cbc6be', fg='#000000', font=('Arial', 14, 'bold'),
                         justify=CENTER)
    title_ranges.place(x=278, y=117)
    title_a = Label(second_menu_panel, text='a', bg='#000000', fg='#ffffff',
                    font=('Franklin Gothic Medium', 14, 'bold'), justify=CENTER)
    title_a.place(x=75, y=155)
    a_entry = Entry(second_menu_panel, width=16, insertbackground='#ff0000', bg='#ffffff', fg='#000000',
                    font=('Franklin Gothic Medium', 14, 'normal'), justify=CENTER)
    a_entry.place(x=98, y=156)
    title_b = Label(second_menu_panel, text='b', bg='#000000', fg='#ffffff',
                    font=('Franklin Gothic Medium', 14, 'bold'),
                    justify=CENTER)
    title_b.place(x=338, y=155)
    b_entry = Entry(second_menu_panel, width=16, insertbackground='#ff0000', bg='#ffffff', fg='#000000',
                    font=('Franklin Gothic Medium', 14, 'normal'), justify=CENTER)
    b_entry.place(x=360, y=156)
    return a_entry, b_entry


def section_parameters(second_menu_panel):
    title_parameters = Label(second_menu_panel, text='Parámetros', bg='#cbc6be', fg='#000000',
                             font=('Arial', 14, 'bold'),
                             justify=CENTER)
    title_parameters.place(x=263, y=221)
    title_po = Label(second_menu_panel, text='| Población inicial |', bg='#000000', fg='#ffffff',
                     font=('Franklin Gothic Medium', 14, 'bold'), justify=CENTER)
    title_po.place(x=75, y=256)
    po_entry = Entry(second_menu_panel, width=24, insertbackground='#ff0000', bg='#ffffff', fg='#000000',
                     font=('Franklin Gothic Medium', 14, 'normal'), justify=CENTER)
    po_entry.place(x=278, y=257)

    title_pm = Label(second_menu_panel, text='Población max.', bg='#000000', fg='#ffffff',
                     font=('Franklin Gothic Medium', 14, 'bold'), justify=CENTER)
    title_pm.place(x=75, y=291)
    pm_entry = Entry(second_menu_panel, width=24, insertbackground='#ff0000', bg='#ffffff', fg='#000000',
                     font=('Franklin Gothic Medium', 14, 'normal'), justify=CENTER)
    pm_entry.place(x=278, y=291)

    # title_pc = Label(second_menu_panel, text='Probabilidad cruce', bg='#000000', fg='#ffffff',
    #                  font=('Franklin Gothic Medium', 14, 'bold'), justify=CENTER)
    # title_pc.place(x=75, y=325)
    # pc_entry = Entry(second_menu_panel, width=24, insertbackground='#ff0000', bg='#ffffff', fg='#000000',
    #                  font=('Franklin Gothic Medium', 14, 'normal'), justify=CENTER)
    # pc_entry.place(x=278, y=325)

    title_pmi = Label(second_menu_panel, text='Prob. mutación ind.', bg='#000000', fg='#ffffff',
                      font=('Franklin Gothic Medium', 14, 'bold'), justify=CENTER)
    title_pmi.place(x=75, y=358)
    pmi_entry = Entry(second_menu_panel, width=24, insertbackground='#ff0000', bg='#ffffff', fg='#000000',
                      font=('Franklin Gothic Medium', 14, 'normal'), justify=CENTER)
    pmi_entry.place(x=278, y=358)

    title_pmg = Label(second_menu_panel, text='Prob. mutación gen', bg='#000000', fg='#ffffff',
                      font=('Franklin Gothic Medium', 14, 'bold'), justify=CENTER)
    title_pmg.place(x=75, y=391)
    pmg_entry = Entry(second_menu_panel, width=24, insertbackground='#ff0000', bg='#ffffff', fg='#000000',
                      font=('Franklin Gothic Medium', 14, 'normal'), justify=CENTER)
    pmg_entry.place(x=278, y=391)
    return po_entry, pm_entry, pmi_entry, pmg_entry  # pc_entry,


def section_results(second_menu_panel):
    title_r = Label(second_menu_panel, text='Resultados', bg='#cbc6be', fg='#000000', font=('Arial', 14, 'bold'),
                    justify=CENTER)
    title_r.place(x=263, y=429)
    title_rd = Label(second_menu_panel, text=' Resultado deseado (Δx)', bg='#000000', fg='#ffffff',
                     font=('Franklin Gothic Medium', 14, 'bold'), justify=CENTER)
    title_rd.place(x=75, y=462)
    rd_entry = Entry(second_menu_panel, width=20, insertbackground='#ff0000', bg='#ffffff', fg='#000000',
                     font=('Franklin Gothic Medium', 14, 'normal'), justify=CENTER)
    rd_entry.place(x=320, y=462)
    return rd_entry


def section_strategies(second_menu_panel):
    title_strategies = Label(second_menu_panel, text='Estrategias', bg='#cbc6be', fg='#000000',
                             font=('Arial', 14, 'bold'),
                             justify=CENTER)
    title_strategies.place(x=263, y=501)

    title_i = Label(second_menu_panel, text='# Iteraciones', bg='#000000', fg='#ffffff',
                    font=('Franklin Gothic Medium', 14, 'bold'), justify=CENTER)
    title_i.place(x=75, y=535)
    i_entry = Entry(second_menu_panel, width=10, insertbackground='#ff0000', bg='#ffffff', fg='#000000',
                    font=('Franklin Gothic Medium', 14, 'normal'), justify=CENTER)
    i_entry.place(x=228, y=535)

    # title_n = Label(second_menu_panel, text='n', bg='#000000', fg='#ffffff',
    #                 font=('Franklin Gothic Medium', 14, 'bold'), justify=CENTER)
    # title_n.place(x=385, y=535)
    # n_entry = Entry(second_menu_panel, width=10, insertbackground='#ff0000', bg='#ffffff', fg='#000000',
    #                 font=('Franklin Gothic Medium', 14, 'normal'), justify=CENTER)
    # n_entry.place(x=430, y=535)
    return i_entry  # , n_entry


def section_optimization(second_menu_panel):
    title_optimization = Label(second_menu_panel, text='Optimización', bg='#cbc6be', fg='#000000',
                               font=('Arial', 14, 'bold'), justify=CENTER)
    title_optimization.place(x=252, y=572)
    optimization_cb = ttk.Combobox(second_menu_panel, width=24, state='readonly',
                                   values=['Minimización', 'Maximización'])
    optimization_cb.place(x=225, y=611)
    return optimization_cb


class Window:
    def __init__(self, window):
        self.window = window
        self.genetic_algorithm = GeneticAlgorithm
        self.graphic = None
        self.csv = None

    def draw_window(self):
        self.window.title("Algoritmo Genetico")
        self.window.geometry("1366x735")
        self.window.config(bg='#2e2e2e')
        self.window.resizable(False, False)

        frame = Frame(self.window)
        frame.pack(fill=BOTH, expand=True)

        first_menu_panel = Label(frame, width=85, height=47, bg='#bababa').place(x=15, y=13)
        second_menu_panel = Label(first_menu_panel, width=83, height=46, bg='#424242').place(x=23, y=20)

        title_menu = Label(second_menu_panel, text='Algoritmo Genético', bg='#cbc6be', fg='#000000',
                           font=('Arial', 14, 'bold'), justify=CENTER)
        title_menu.place(x=218, y=26)

        # Equation
        # equation_entry = Entry(second_menu_panel, width=32, insertbackground='#ff0000', bg='#ffffff', fg='#000000',
        #                        font=('Franklin Gothic Medium', 14, 'italic'), justify=CENTER)
        # equation_entry.place(x=135, y=65)
        # title_equation = Label(second_menu_panel, text='f(x)', bg='#000000', fg='#ffffff',
        #                        font=('Franklin Gothic Medium', 14, 'bold'), justify=CENTER)
        # title_equation.place(x=90, y=69)

        # Ranges
        a_entry, b_entry = section_ranges(second_menu_panel)
        # cp_entry,
        # Parameters
        ip_entry, mp_entry, imp_entry, gmp_entry = section_parameters(second_menu_panel)

        # Results
        dr_entry = section_results(second_menu_panel)
        # , n_entry
        # Strategies
        i_entry = section_strategies(second_menu_panel)

        # Optimization
        optimization = section_optimization(second_menu_panel)

        graphic_panel_one = Label(frame, width=102, height=23, bg='#543030').place(x=630, y=13)
        graphic_panel_two = Label(frame, width=102, height=23, bg='#094428').place(x=630, y=373)
        canvas_graphics = Canvas(self.window, background="#094428")
        canvas_graphics.pack(fill="both", expand=True)

        scrollbar_vertical = Scrollbar(canvas_graphics, orient="vertical", command=canvas_graphics.yview)
        scrollbar_vertical.pack(side="right", fill="y")

        canvas_graphics.configure(yscrollcommand=scrollbar_vertical.set)

        frame_inner = Frame(canvas_graphics)
        canvas_graphics.create_window((0, 0), window=frame_inner, anchor="nw")

        canvas_graphics.place(anchor="nw", width=720, height=351, x=630, y=373, bordermode="inside")

        entries = {"smp": second_menu_panel,
                   "ip": ip_entry,
                   "mp": mp_entry,
                   # "cp": cp_entry,
                   "imp": imp_entry,
                   "gmp": gmp_entry,
                   "a": a_entry,
                   "b": b_entry,
                   "dr": dr_entry,
                   "i": i_entry,
                   # "n": n_entry,
                   "optimization": optimization,
                   "gpo": graphic_panel_one,
                   "gpt": canvas_graphics,
                   "f": frame_inner}

        # Buttons
        self.section_buttons(entries)

    def section_buttons(self, entries):
        Button(entries["smp"], width=12, text='Resolver', bg='#850000', fg='#ffffff',
               command=lambda: self.execute_genetic_algorithm(entries),
               font=('Franklin Gothic Medium', 14, 'bold')).place(x=75, y=650)

        Button(entries["smp"], width=12, text='Ver gráficas', bg='#064c1b', fg='#ffffff',
               command=lambda: self.graphic.show_graphics(entries["a"].get(), entries["b"].get(),
                                                          entries["optimization"].get()),
               font=('Franklin Gothic Medium', 14, 'bold')).place(x=245, y=650)

        Button(entries["smp"], width=12, text='CSV', bg='#828500', fg='#ffffff',
               command=lambda: self.csv.download_csv(),
               font=('Franklin Gothic Medium', 14, 'bold')).place(x=420, y=650)

    def execute_genetic_algorithm(self, entries):
        population, statistic, population_for_generation, population_for_generation_before_poda, pg = self.genetic_algorithm(
            entries).genetic_algorithm()
        self.graphic = Graphic(self.window, entries["gpo"], entries["gpt"], entries["f"], statistic,
                               population_for_generation, population_for_generation_before_poda, pg)
        self.csv = Result(pg, statistic)
