from Triangle import Triangle

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimension(self):
        return "3D"

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return super()._square()

    def volume(self):
        return (self.squareBase() * self.h) / 3

    def __str__(self):
        return (
            f"TriangularPyramid(a={self.a}, h={self.h}), "
            f"Dimension: {self.dimension()}, "
            f"Perimeter: {self.perimeter()}, "
            f"Square: {self.square()}, "
            f"SquareSurface: {self.squareSurface()}, "
            f"SqureBase: {self.squareBase():3.2f}, "
            f"Heigt: {self.height()}, "
            f"Volume: {self.volume():3.2f}"
        )

if __name__ == "__main__":
    tp1 = TriangularPyramid(3, 3)
    print(tp1)