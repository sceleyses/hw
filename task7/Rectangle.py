from Figure import Figure

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dimension(self):
        return "2D"

    def perimeter(self):
        return 2 * (self.a + self.b)

    def _square(self):
        return self.a * self.b

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return super().volume()

    def __str__(self):
        return (
            f"Rectangle(a = {self.a}, b = {self.b}), "
            f"Dimension: {self.dimension()}, "
            f"Perimeter: {self.perimeter():3.2f}, "
            f"Square: {self.square():3.2f}, "
            f"SquareSurface: {self.squareSurface()}, "
            f"SqureBase: {self.squareBase()}, "
            f"Heigt: {self.height()}, "
            f"Volume: {self.volume():3.2f}"
        )

if __name__ == "__main__":
    r1 = Rectangle(3, 3)
    print(r1)
