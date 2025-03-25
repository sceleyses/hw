from Rectangle import Rectangle

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
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
        return None

    def height(self):
        return self.h

    def volume(self):
        return (super()._square() * self.h) / 3

    def __str__(self):
        return (
            f"QuadrangularPyramid(a = {self.a}, b = {self.b}, h = {self.h}), "
            f"Dimension: {self.dimension()}, "
            f"Perimeter: {self.perimeter()}, "
            f"Square: {self.square()}, "
            f"SquareSurface: {self.squareSurface()}, "
            f"SqureBase: {self.squareBase()}, "
            f"Heigt: {self.height():3.2f}, "
            f"Volume: {self.volume():3.2f}"
        )

if __name__ == "__main__":
    p = QuadrangularPyramid(3, 4, 5)
    print(p)