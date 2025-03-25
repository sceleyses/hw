from Circle import Circle
import  math
class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h

    def dimension(self):
        return "3D"

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return math.pi * self.r * (self.r**2 + self.h**2)**0.5

    def squareBase(self):
        return None

    def height(self):
        return self.h

    def volume(self):
        return (super()._square() * self.h) / 3

    def __str__(self):
        return (
            f"Cone(r = {self.r}, h = {self.h}),  "
            f"Circle(r = {self.r}),  "
            f"Dimension: {self.dimension()}, "
            f"Perimeter: {self.perimeter()}, "
            f"Square: {self.square()}, "
            f"SquareSurface: {self.squareSurface():3.2f}, "
            f"SqureBase: {self.squareBase()}, "
            f"Heigt: {self.height()}, "
            f"Volume: {self.volume():3.2f}"
        )
if __name__ == "__main__":
    c1 = Cone(3, 3)
    print(c1)