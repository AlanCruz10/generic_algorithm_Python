import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *
import imageio
import mplcursors
import os
import numpy as np
import utilities.utility as utility
import cv2


def restore_zoom(toolbar):
    toolbar.home()


def make_video_and_gif_from_graphics():
    input_folder = 'graphics/generations/'
    output_folder = 'graphics/video/'
    os.makedirs(output_folder, exist_ok=True)

    file_names = sorted(
        [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.png')],
        key=lambda x: int(x.split('generation_')[1].split('.png')[0])
    )

    output_video = 'graphics/video/generations.mp4'

    first_image = cv2.imread(file_names[0])
    height, width, layers = first_image.shape

    fps = 0.5

    video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))
    for file in file_names:
        img = cv2.imread(file)
        video.write(img)

    video.release()

    input_folder2 = 'graphics/generations/'
    output_folder2 = 'graphics/gif/'
    os.makedirs(output_folder2, exist_ok=True)

    file_names2 = sorted(
        [os.path.join(input_folder2, file) for file in os.listdir(input_folder2) if file.endswith('.png')],
        key=lambda x: int(x.split('generation_')[1].split('.png')[0]))

    output_gif = 'graphics/gif/generations.gif'

    images = [imageio.imread_v2(file) for file in file_names2]
    imageio.mimsave(output_gif, images)


class Graphic:
    def __init__(self, window, frame_one, frame_two, frame_inner, list_statistics, pfg, pfgb, pg):
        self.window = window
        self.frame_one = frame_one
        self.frame_two = frame_two
        self.frame_inner = frame_inner
        self.list_statistics = list_statistics
        # self.pfg = pfg
        # self.pfgb = pfgb
        self.pg = pg
        # self.population = population
        # self.pr = pruning

    def show_graphics(self, a, b, optimization):
        self.show_graphic_fitness_by_generation()
        self.show_graphic_statistics_by_generation(a, b, optimization)
        make_video_and_gif_from_graphics()

    def show_graphic_fitness_by_generation(self):
        output_folder = 'graphics/statistics/'
        os.makedirs(output_folder, exist_ok=True)

        iterations_for_graphic = list(range(0, len(self.list_statistics)))

        bests = [s["best"].fx for s in self.list_statistics]
        worsts = [s["worst"].fx for s in self.list_statistics]
        averages = [s["average"] for s in self.list_statistics]

        fig, ax = plt.subplots(figsize=(12, 5.9), dpi=60)
        # ,  , marker='s' , marker='o'
        ax.plot(iterations_for_graphic, bests, label='Mejores resultados', marker='^', linestyle='-')
        ax.plot(iterations_for_graphic, worsts, label='Peores resultados', marker='s', linestyle='--',
                color='orange')
        ax.plot(iterations_for_graphic, averages, label='Promedio', marker='o', linestyle='-.',
                color='green')
        ax.set_xticks(range(len(iterations_for_graphic)), labels=iterations_for_graphic, rotation=30)
        ax.set_title('Evolucion a lo largo de las generaciones')
        ax.set_xlabel('Generaciones')
        ax.set_ylabel('Fitness')
        ax.legend()
        filename = os.path.join(output_folder, 'graphics_statistics.png')
        fig.savefig(filename)
        mplcursors.cursor(hover=True)
        canvas_figure = FigureCanvasTkAgg(fig, master=self.frame_one)
        canvas_figure.draw()
        canvas_figure_widget = canvas_figure.get_tk_widget()
        canvas_figure_widget.place(x=630, y=13)
        toolbar = NavigationToolbar2Tk(canvas_figure, self.frame_one)
        toolbar.zoom(10)
        toolbar.place(x=2000, y=0)

    def show_graphic_statistics_by_generation(self, a, b, optimization):
        output_folder = 'graphics/generations/'
        if os.path.exists(output_folder):
            for file_name in os.listdir(output_folder):
                file_path = os.path.join(output_folder, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f'Error al eliminar {file_path}: {e}')

        os.makedirs(output_folder, exist_ok=True)
        for key, value in self.pg.items():
            fx = [g.fx for g in self.pg[key][0]]
            x = [g.x for g in self.pg[key][0]]

            fig, ax = plt.subplots(figsize=(11.68, 5.78), dpi=60)
            ax.spines['left'].set_position('zero')
            ax.spines['left'].set_color('gray')
            ax.spines['bottom'].set_position('zero')
            ax.spines['bottom'].set_color('gray')

            x_l = [[ge.x for ge in self.pg[k][0]] for k, v in self.pg.items()]
            fx_l = [[ge.fx for ge in self.pg[k][0]] for k, v in self.pg.items()]

            fx_min = min([min(fx_ll) for fx_ll in [fx_list for fx_list in fx_l]])
            fx_max = max([max(fx_ll) for fx_ll in [fx_list for fx_list in fx_l]])

            points = max([len(x_list) for x_list in x_l])
            x_range = np.linspace(float(a), float(b), points)
            func_values = utility.evaluation_function(x_range)

            ax.plot(x_range, func_values, label='Funcion', color='black', linestyle='--')

            if fx_min >= 0:
                ax.set_xlim((float(a)) - 1, (float(b) + 1))
                if fx_min == 0:
                    ax.set_ylim((0 - 1), (fx_max + 1))
                else:
                    ax.set_ylim(0, (fx_max + 1))
            else:
                ax.set_xlim((float(a)) - 1, (float(b) + 1))
                ax.set_ylim((fx_min - 1), (fx_max + 1))

            ax.scatter(x, fx, color='blue', label=f'Poblacion {key}')
            idx_max = np.argmax(fx)
            idx_min = np.argmin(fx)
            if optimization == "Maximización":
                ax.scatter(x[idx_max], fx[idx_max], color='green', marker='o', label='Mejor')
                ax.scatter(x[idx_min], fx[idx_min], color='red', marker='x', label='Peor')
            else:
                ax.scatter(x[idx_min], fx[idx_min], color='green', marker='o', label='Mejor')
                ax.scatter(x[idx_max], fx[idx_max], color='red', marker='x', label='Peor')
            ax.set_xlabel('Rango')
            ax.set_ylabel('fx')
            ax.set_title(f'Generación {key}')
            ax.legend()
            ax.grid(True, linewidth=0.5, color='gray', alpha=0.7)
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            filename = os.path.join(output_folder, f'graphics_generation_{key}.png')
            fig.savefig(filename)
            mplcursors.cursor(hover=True)
            canvas_figure = FigureCanvasTkAgg(fig, master=self.frame_inner)
            canvas_figure.draw()
            canvas_figure_widget = canvas_figure.get_tk_widget()
            canvas_figure_widget.pack()
            toolbar = NavigationToolbar2Tk(canvas_figure, self.frame_inner)
            toolbar.zoom(10)
            toolbar.place(x=2000, y=0)

        self.frame_inner.update_idletasks()
        bbox = self.frame_two.bbox(ALL)
        self.frame_two.configure(scrollregion=bbox)
