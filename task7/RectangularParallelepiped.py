from Rectangle import Rectangle

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.depth = h

    def dimension(self):
        return "3D"

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return 2 * (
                self.a * self.b +
                self.a * self.depth +
                self.b * self.depth
            )

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.a * self.b * self.depth

    def __str__(self):
        return (
            f"RectangularParallelepiped(a = {self.a}, b = {self.b}, h = {self.depth}), "
            f"Dimension: {self.dimension()}, "
            f"Perimeter: {self.perimeter()}, "
            f"Square: {self.square()}, "
            f"SquareSurface: {self.squareSurface():3.2f}, "
            f"SqureBase: {self.squareBase()}, "
            f"Heigt: {self.height()}, "
            f"Volume: {self.volume():3.2f}"
        )

if __name__ == "__main__":
    rp = RectangularParallelepiped(3, 4, 5)
    print(rp)