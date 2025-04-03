class Rational:
    def __init__(self,numerator, denumerator=1 ):
        self.n = numerator
        self.d = denumerator

    def __add__(self, other):
        new_n = self.n * other.d + other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __sub__(self, other):
        new_n = self.n * other.d - other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __mul__(self, other):
        new_n = self.n * other.n
        new_d = self.d * other.d
        return Rational(new_n, new_d)


    def __str__(self):
            return f"{self.n}/{self.d}"

if __name__ == "__main__":
    r1 = Rational(5)
    r2 = Rational(3)
    print(r1 * r2)
