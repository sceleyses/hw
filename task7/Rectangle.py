class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dimension(self):
        return "2d"

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()

    def __str__(self):
        return (
            f"Rectangle(a = {self.a}, b = {self.b}), "
            f"Perimeter: {self.perimeter()}, "
            f"Square: {self.square():.2f}"
        )

if __name__ == "__main__":
    r1 = Rectangle(3, 3)
    print(r1)
