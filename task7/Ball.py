from Figure import Figure
import math

class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return "3D"

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return 4 * math.pi * self.r ** 2

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return (4/3) * math.pi * self.r ** 3

    def __str__(self):
        return (
            f"Ball(r = {self.r}), "
            f"Dimension: {self.dimension()}, "
            f"Perimeter: {self.perimeter()}, "
            f"Square: {self.square()}, "
            f"SquareSurface: {self.squareSurface():3.2}, "
            f"SqureBase: {self.squareBase()}, "
            f"Heigt: {self.height()}, "
            f"Volume: {self.volume():3.2f}"
        )

if __name__ == "__main__":
    b1 = Ball(3)
    print(b1)

