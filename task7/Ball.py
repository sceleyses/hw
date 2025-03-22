from Figure import Figure
import math

class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return "3D"

    def squareSurface(self):
        return 4 * math.pi * self.r ** 2

    def volume(self):
        return (4/3) * math.pi * self.r ** 3

    def __str__(self):
        return (
            f"Ball(r = {self.r}), "
            f"Perimeter: {self.squareSurface()}, "
            f"Square: {self.volume():.2f}"
        )

if __name__ == "__main__":
    b1 = Ball(3)
    print(b1)

