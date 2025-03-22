class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def dimension(self):
        return "2D"

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def __str__(self):
        return (
            f"parallelogram(a = {self.a}, b = {self.b}, h = {self.h}),  "
            f"Perimeter: {self.perimeter()}, "
            f"Square: {self.square():.2f}"
        )

if __name__ == "__main__":
    p1 = Parallelogram(3, 3, 3)
    print(p1)
