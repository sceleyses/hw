from Figure import Figure

class Trapeze(Figure):

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def dimension(self):
        return "2D"

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        return (self.a + self.b) * self.height() / 2

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return (self.c**2 - ((self.a - self.b)/2)**2)**0.5

    def volume(self):
        return super().volume()


    def __str__(self):
        return (
            f"Trapeze(a = {self.a}, b = {self.b}, c = {self.c}, d = {self.d}), "
            f"Dimension: {self.dimension()}, "
            f"Perimeter: {self.perimeter():3.2f}, "
            f"Square: {self.square():3.2f}, "
            f"SquareSurface: {self.squareSurface()}, "
            f"SqureBase: {self.squareBase()}, "
            f"Heigt: {self.height()}, "
            f"Volume: {self.volume():3.2f}"
        )


if __name__ == "__main__":
    t1 = Trapeze(3, 3, 3, 3)
    print(t1)