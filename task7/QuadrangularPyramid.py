from Rectangle import Rectangle

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimension(self):
        return "3D"

    def volume(self):
        return (self.square() * self.h) / 3

    def __str__(self):
        return (
            f"QuadrangularPyramid(a = {self.a}, b = {self.b}, h = {self.h}), "
            f"Volume: {self.volume():.2f}"
        )

if __name__ == "__main__":
    p = QuadrangularPyramid(3, 4, 5)
    print(p)