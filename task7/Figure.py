class Figure:
    def dimension(self):
        pass

    def perimeter(self):
        pass

    def square(self):
        pass

    def squareSurface(self):
        pass

    def squareBase(self):
        pass

    def height(self):
        pass

    def volume(self):
        if self.dimension() == "2D":
            return self.square()
        else:
            return 0.0