from Figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def dimension(self):
        return "2d"

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5

    def volume(self):
        return self.square()

    def __str__(self):
        return (
            f"Triangle(a = {self.a}, b = {self.b}, c = {self.c}), "
            f"Perimeter: {self.perimeter()}, "
            f"Square: {self.square():.2f}"
        )

if __name__ == "__main__":
    t1 = Triangle(3, 3, 3)
    print(t1)

