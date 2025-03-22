from Triangle import Triangle
class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimension(self):
        return "3D"

    def squareBase(self):
        return self.square()

    def volume(self):
        return (self.squareBase() * self.h) / 3

    def __str__(self):
        return (
            f"TriangularPyramid(a={self.a}, h={self.h}), "
            f"Base Square: {self.squareBase():.2f}, "
            f"Volume: {self.volume():.2f}"
        )

if __name__ == "__main__":
    tp1 = TriangularPyramid(3, 3)
    print(tp1)