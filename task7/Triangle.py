from Figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def dimension(self):
        return "2D"

    def _perimeter(self):
        return self.a + self.b + self.c

    def _square(self):
        p = self._perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5

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
            f"Triangle(a = {self.a}, b = {self.b}, c = {self.c}), "
            f"Dimension: {self.dimension()}, "
            f"Perimeter: {self.perimeter():3.2f}, "
            f"Square: {self.square():3.2f}, "
            f"SquareSurface: {self.squareSurface()}, "
            f"SqureBase: {self.squareBase()}, "
            f"Heigt: {self.height()}, "
            f"Volume: {self.volume():3.2f}"
        )

if __name__ == "__main__":
    t1 = Triangle(3, 3, 3)
    print(t1)

