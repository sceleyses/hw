from Ball import Ball
from Circle import Circle
from Cone import Cone
from Parallelogram import Parallelogram
from QuadrangularPyramid import QuadrangularPyramid
from Rectangle import Rectangle
from RectangularParallelepiped import RectangularParallelepiped
from Trapeze import Trapeze
from Triangle import Triangle
from TriangularPrism import TriangularPrism
from TriangularPyramid import TriangularPyramid
import math


def ProcessFigures(file_name):
    figures = []
    with open(file_name) as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue

            name = parts[0]
            try:
                params = list(map(float, parts[1:]))
                if name == "Triangle":
                    fig = Triangle(*params)
                elif name == "Rectangle":
                    fig = Rectangle(*params)
                elif name == "Trapeze":
                    fig = Trapeze(*params)
                elif name == "Parallelogram":
                    fig = Parallelogram(*params)
                elif name == "Circle":
                    fig = Circle(*params)
                elif name == "Ball":
                    fig = Ball(*params)
                elif name == "TriangularPyramid":
                    fig = TriangularPyramid(*params)
                elif name == "TriangularPrism":
                    fig = TriangularPrism(*params)
                elif name == "QuadrangularPyramid":
                    fig = QuadrangularPyramid(*params)
                elif name == "RectangularParallelepiped":
                    fig = RectangularParallelepiped(*params)
                elif name == "Cone":
                    fig = Cone(*params)
                else:
                    raise ValueError(f"Невідома фігура: {name}")

                figures.append(fig)

            except Exception:
                continue

    return figures

def WriteFile(file_name, figures):
    valid_figures = []
    for fig in figures:
        vol = fig.volume()
        if isinstance(vol, (int, float)) and not math.isnan(vol):
            valid_figures.append(fig)

    with open(file_name, 'w') as f:
        max_figure = max(valid_figures, key=lambda fig: fig.volume())

        f.write(f"Type: {max_figure.__class__.__name__}\n")
        f.write(f"Parameters: {vars(max_figure)}\n")
        f.write(f"Measure: {max_figure.volume():.2f}\n")


figures = ProcessFigures("input01.txt")
WriteFile("output01.txt", figures)

