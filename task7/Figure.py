class Figure:
    def dimension(self):
        return "Unknown"

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        if self.dimension() == "2D":
            return self.square()
        else:
            return 0.0