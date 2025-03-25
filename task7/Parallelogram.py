from Figure import Figure

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def dimension(self):
        return "2D"

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def square(self):
        return self.a * self.b

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return self.h

    def volume(self):
        return super().volume()

    def __str__(self):
        return (
            f"parallelogram(a = {self.a}, b = {self.b}, h = {self.h}),  "
            f"Dimension: {self.dimension()}, "
            f"Perimeter: {self.perimeter():3.2f}, "
            f"Square: {self.square():3.2f}, "
            f"SquareSurface: {self.squareSurface()}, "
            f"SqureBase: {self.squareBase()}, "
            f"Heigt: {self.height()}, "
            f"Volume: {self.volume():3.2f}"
        )

if __name__ == "__main__":
    p1 = Parallelogram(3, 3, 3)
    print(p1)
