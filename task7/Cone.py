from Circle import Circle
import  math
class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h

    def dimension(self):
        return "3D"

    def squareSurface(self):
        return math.pi * self.r * (self.r**2 + self.h**2)**0.5

    def volume(self):
        return (super().square() * self.h) / 3

    def __str__(self):
        return (
            f"Cone(r = {self.r}, h = {self.h}),  "
            f"Perimeter: {self.perimeter()}, "
            f"Square: {self.square():.2f}"
        )
if __name__ == "__main__":
    c1 = Cone(3, 3)
    print(c1)