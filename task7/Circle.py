from Figure import Figure
import math
class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return "2D"

    def perimeter(self):
        return 2 * math.pi * self.r

    def _square(self):
        return math.pi * self.r ** 2

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()

    def __str__(self):
        return (
            f"Circle(r = {self.r}),  "
            f"Dimension: {self.dimension()}, "
            f"Perimeter: {self.perimeter():3.2f}, "
            f"Square: {self.square():3.2f}, "
            f"SquareSurface: {self.squareSurface()}, "
            f"SqureBase: {self.squareBase()}, "
            f"Heigt: {self.height()}, "
            f"Volume: {self.volume():3.2f}"
        )

if __name__ == "__main__":
    c1 = Circle(3)
    print(c1)

