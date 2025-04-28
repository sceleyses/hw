from Matrix2D import Matrix2D
from Vector2D import Vector2D


class Solver:
    def __init__(self, a: Matrix2D, b: Vector2D):
        self.a = a
        self.b = b

    def __str__(self):
        return f"A:\n{self.a}\nB: {self.b}"

    def solve(self):
        if self.a.is_degenerate():
            return None
        d = self.a.det()
        m1 = Matrix2D(self.b, self.a.col(2))
        d1 = m1.det()
        m2 = Matrix2D(self.a.col(1), self.b)
        d2 = m2.det()
        return Vector2D(d1 / d, d2 / d)

if __name__ == '__main__':
    A = Matrix2D(1, 2, 2, 1)
    b = Vector2D(4, 5)
    # s = Solver(A, b)
    print(s)
    print("=== A ====")
    print(A)
    print("=== b ====")
    print(b)
    x = s.solve()
    print(x)