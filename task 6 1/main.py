from Matrix2D import Matrix2D
from Vector2D import Vector2D
from Solver import Solver
import sys


matrices = []
vectors = []

try:
    with open("matrix_coefficients.txt", "r", encoding="utf-8") as f:
        for line in f:
            elements = list(map(float, line.strip().split()))
            if len(elements) == 4:
                matrices.append(Matrix2D(elements))
except FileNotFoundError:
    print(f"Файл не знайдено")
    sys.exit(1)

try:
    with open("rhs_values.txt", "r", encoding="utf-8") as f:
        for line in f:
            elements = list(map(float, line.strip().split()))
            if len(elements) == 2:
                vectors.append(Vector2D(elements))
except FileNotFoundError:
    print(f"Файл не знайдено")
    sys.exit(1)

if len(matrices) != len(vectors):
    print("Помилка: кількість матриць і векторів не співпадає")
    sys.exit(1)

output = []
for mat, vec in zip(matrices, vectors):
    solver = Solver(mat, vec)
    solution = solver.solve()
    output.append(str(solution) if solution else "Система не має розв'язку")

with open("results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output))
