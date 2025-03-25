from Triangle import Triangle

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimension(self):
        return "3D"

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return (super()._perimeter() * self.h)+ 2 * super()._square()

    def squareBase(self):
        return None

    def height(self):
        return self.h

    def volume(self):
        return super()._square() * self.h


    def __str__(self):
        return (
            f"TriangularPrism(a={self.a}, b={self.b}, c={self.c}, h={self.h}), "
            f"Dimension: {self.dimension()}, "
            f"Perimeter: {self.perimeter()}, "
            f"Square: {self.square()}, "
            f"SquareSurface: {self.squareSurface():3.2f}, "
            f"SqureBase: {self.squareBase()}, "
            f"Heigt: {self.height():3.2f}, "
            f"Volume: {self.volume():3.2f}"
        )

if __name__ == "__main__":
    tp = TriangularPrism(3, 4, 5, 10)
    print(tp)