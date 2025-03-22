from Triangle import Triangle

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimension(self):
        return "3D"

    def squareSurface(self):
        return self.perimeter() * self.h

    def volume(self):
        return self.square() * self.h

    def totalSurfaceArea(self):
        return self.squareSurface() + 2 * self.square()

    def __str__(self):
        return (
            f"TriangularPrism(a={self.a}, b={self.b}, c={self.c}, h={self.h}), "
            f"Lateral Surface Area: {self.squareSurface():.2f}, "
            f"Total Surface Area: {self.totalSurfaceArea():.2f}, "
            f"Volume: {self.volume():.2f}"
        )

if __name__ == "__main__":
    tp = TriangularPrism(3, 4, 5, 10)
    print(tp)