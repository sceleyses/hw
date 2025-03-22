import math
class Circle:
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return "2D"

    def perimeter(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

    def __str__(self):
        return (
            f"Circle(r = {self.r}),  "
            f"Perimeter: {self.perimeter()}, "
            f"Square: {self.square():.2f}"
        )

if __name__ == "__main__":
    c1 = Circle(3)
    print(c1)

