from Rectangle import Rectangle

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.depth = h

    def dimension(self):
        return "3D"

    def squareSurface(self):
        return 2 * (
                self.a * self.b +
                self.a * self.depth +
                self.b * self.depth
            )

    def volume(self):
        # Об'єм: довжина * ширина * висота
        return self.a * self.b * self.depth

    def __str__(self):
        return (
            f"RectangularParallelepiped(a = {self.a}, b = {self.b}, h = {self.depth}), "
            f"Surface Area: {self.squareSurface():.2f}, "
            f"Volume: {self.volume():.2f}"
        )

if __name__ == "__main__":
    rp = RectangularParallelepiped(3, 4, 5)
    print(rp)